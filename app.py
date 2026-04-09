import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


# 🔹 Rota principal (buscar clima)
@app.route("/", methods=["GET", "POST"])
def index():
    clima = None

    if request.method == "POST":
        cidade = request.form.get("cidade")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            clima = {
                "cidade": dados["name"],
                "temperatura": dados["main"]["temp"],
                "descricao": dados["weather"][0]["description"],
                "icone": dados["weather"][0]["icon"]  # 🔥 CORREÇÃO DO ÍCONE
            }
        else:
            clima = {"erro": "Cidade não encontrada"}

    return render_template("index.html", clima=clima)


# 🔹 Rota para autocomplete de cidades
@app.route("/buscar_cidades")
def buscar_cidades():
    query = request.args.get("q")

    if not query:
        return jsonify([])

    url = f"https://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={API_KEY}"
    resposta = requests.get(url)

    cidades = []

    if resposta.status_code == 200:
        dados = resposta.json()

        for cidade in dados:
            nome = f"{cidade['name']}, {cidade.get('state', '')}, {cidade['country']}"
            cidades.append(nome)

    return jsonify(cidades)


# 🔹 Rodar servidor
if __name__ == "__main__":
    app.run(debug=True)