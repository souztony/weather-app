from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "de42efaa40dd70c4ec310afa5c3bf0b2"

@app.route("/", methods=["GET", "POST"])
def index():
    clima = None

    if request.method == "POST":
        cidade = request.form.get("cidade")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            clima = {
                "cidade": dados["name"],
                "temperatura": dados["main"]["temp"],
                "descricao": dados["weather"][0]["description"]
            }
        else:
            clima = {"erro": "Cidade não encontrada"}

    return render_template("index.html", clima=clima)

if __name__ == "__main__":
    app.run(debug=True)