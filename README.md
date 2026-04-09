# Weather App 🌍

Este é um projeto de aplicação web de previsão do tempo desenvolvido utilizando a biblioteca **Flask** e a API gratuita do **Open-Meteo**, garantindo o funcionamento imediato sem a necessidade de chaves de autenticação.

## Funcionalidades
- **Busca de Clima**: Permite aos usuários obter informações em tempo real sobre a temperatura, descrição do clima e um ícone visual correspondente a qualquer cidade pesquisada.
- **Sugestões de Autocomplete**: Quando o usuário começa a digitar o nome da cidade, o aplicativo sugere nomes de cidades (com estado e país) para facilitar a precisão da busca.
- **Tratamento de Erros**: Caso o usuário insira o nome de uma cidade inexistente ou o serviço fique indisponível, um feedback de erro claro é retornado.

## Bibliotecas e Tecnologias
- [Flask](https://flask.palletsprojects.com/) - Framework web para a criação das rotas e servidor.
- [requests](https://docs.python-requests.org/) - Para realizar requisições HTTP para a API do Open-Meteo.
- HTML, CSS, JavaScript (Vanilla) - Para a interface, estilos visuais e requisições assíncronas do autocomplete.

## Como Executar

1. **Clone o repositório** ou extraia os arquivos para um diretório.
2. Certifique-se de ter o Python instalado em seu computador.
3. **Instale as dependências** do projeto usando o comando no terminal:
   ```bash
   pip install -r requirements.txt
   ```
4. **Inicie o servidor Flask**:
   ```bash
   python app.py
   ```
5. Abra o navegador e acesse a aplicação em `http://127.0.0.1:5000`.

---
*Desenvolvido por Tony Souz*
