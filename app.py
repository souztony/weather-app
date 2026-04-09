from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)

def get_weather_info(code, is_day):
    suffix = "d" if is_day == 1 else "n"
    
    weather_codes = {
        0: ("Céu limpo", f"01{suffix}"),
        1: ("Pouco nublado", f"02{suffix}"),
        2: ("Parcialmente nublado", f"03{suffix}"),
        3: ("Nublado", f"04{suffix}"),
        45: ("Névoa", f"50{suffix}"),
        48: ("Névoa com geada", f"50{suffix}"),
        51: ("Garoa leve", f"09{suffix}"),
        53: ("Garoa moderada", f"09{suffix}"),
        55: ("Garoa intensa", f"09{suffix}"),
        56: ("Garoa congelante leve", f"09{suffix}"),
        57: ("Garoa congelante intensa", f"09{suffix}"),
        61: ("Chuva leve", f"10{suffix}"),
        63: ("Chuva moderada", f"10{suffix}"),
        65: ("Chuva intensa", f"10{suffix}"),
        66: ("Chuva congelante leve", f"13{suffix}"),
        67: ("Chuva congelante intensa", f"13{suffix}"),
        71: ("Queda de neve leve", f"13{suffix}"),
        73: ("Queda de neve moderada", f"13{suffix}"),
        75: ("Queda de neve intensa", f"13{suffix}"),
        77: ("Grãos de neve", f"13{suffix}"),
        80: ("Pancadas de chuva leve", f"09{suffix}"),
        81: ("Pancadas de chuva moderada", f"09{suffix}"),
        82: ("Pancadas de chuva violenta", f"09{suffix}"),
        85: ("Pancadas de neve leve", f"13{suffix}"),
        86: ("Pancadas de neve intensa", f"13{suffix}"),
        95: ("Tempestade leve/moderada", f"11{suffix}"),
        96: ("Tempestade com granizo leve", f"11{suffix}"),
        99: ("Tempestade com granizo intenso", f"11{suffix}"),
    }
    return weather_codes.get(code, ("Desconhecido", f"03{suffix}"))


# 🔹 Rota principal (buscar clima)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cidade_input = request.form.get("cidade", "")
        return redirect(url_for("index", cidade=cidade_input))

    clima = None
    cidade_input = request.args.get("cidade")

    if cidade_input:

        partes_input = [p.strip() for p in cidade_input.split(",")]
        cidade_busca = partes_input[0]

        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade_busca}&count=10&language=pt"
        geo_resposta = requests.get(geo_url)

        if geo_resposta.status_code == 200:
            geo_dados = geo_resposta.json()
            if "results" in geo_dados and len(geo_dados["results"]) > 0:
                
                resultado = geo_dados["results"][0]
                
                if len(partes_input) > 1:
                    for res in geo_dados["results"]:
                        estado = res.get("admin1", "")
                        pais = res.get("country", "")
                        if estado in partes_input or pais in partes_input:
                            resultado = res
                            break
                            
                lat = resultado["latitude"]
                lon = resultado["longitude"]
                
                partes_exibicao = [resultado["name"]]
                if resultado.get("admin1"): partes_exibicao.append(resultado["admin1"])
                if resultado.get("country"): partes_exibicao.append(resultado["country"])
                nome_cidade = ", ".join(partes_exibicao)
                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
                weather_resposta = requests.get(weather_url)

                if weather_resposta.status_code == 200:
                    weather_dados = weather_resposta.json()
                    current = weather_dados["current_weather"]
                    
                    is_day = current.get("is_day", 1)  # Se não vier na API, assume dia
                    descricao, icone = get_weather_info(current["weathercode"], is_day)

                    clima = {
                        "cidade": nome_cidade.strip(", "),
                        "temperatura": current["temperature"],
                        "descricao": descricao,
                        "icone": icone
                    }
                else:
                    clima = {"erro": "Erro ao buscar detalhes do clima."}
            else:
                clima = {"erro": "Cidade não encontrada"}
        else:
            clima = {"erro": "Serviço de geolocalização indisponível."}

    return render_template("index.html", clima=clima)


# 🔹 Rota para autocomplete de cidades
@app.route("/buscar_cidades")
def buscar_cidades():
    query = request.args.get("q")

    if not query:
        return jsonify([])

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={query}&count=5&language=pt"
    resposta = requests.get(url)

    cidades = []

    if resposta.status_code == 200:
        dados = resposta.json()
        if "results" in dados:
            for cidade in dados["results"]:
                estado = cidade.get('admin1', '')
                pais = cidade.get('country', '')
                
                partes = [cidade["name"]]
                if estado: partes.append(estado)
                if pais: partes.append(pais)
                    
                nome = ", ".join(partes)
                cidades.append(nome)

    return jsonify(cidades)


# 🔹 Rodar servidor
if __name__ == "__main__":
    app.run(debug=True)