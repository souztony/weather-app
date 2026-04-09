# Weather App 🌍

Este é um projeto desenvolvido como tarefa prática para o curso "Python Pro". Consiste em uma aplicação web de previsão do tempo utilizando a biblioteca **Flask** e a API do **OpenWeatherMap**.

## Funcionalidades
- **Busca de Clima**: Permite aos usuários obter informações em tempo real sobre a temperatura, descrição do clima e um ícone visual correspondente a qualquer cidade pesquisada.
- **Sugestões de Autocomplete**: Quando o usuário começa a digitar o nome da cidade, o aplicativo sugere nomes de cidades para facilitar a busca.
- **Tratamento de Erros**: Caso o usuário insira o nome de uma cidade inexistente, um feedback adequado é retornado ("Cidade não encontrada").

## Bibliotecas e Tecnologias
- [Flask](https://flask.palletsprojects.com/) - Framework web para a criação das rotas.
- [requests](https://docs.python-requests.org/) - Para realizar requisições HTTP para a API do OpenWeatherMap.
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Para carregamento e proteção da chave de API (`API_KEY`).
- HTML, CSS, JavaScript (Vanilla) - Para a interface, estilos visuais e requisições assíncronas do autocomplete.

## Como Executar

1. **Clone o repositório** ou extraia os arquivos para um diretório.
2. Certifique-se de ter o Python instalado em seu computador.
3. **Instale as dependências** do projeto usando o comando:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` na raiz do projeto (se não existir) e adicione a sua chave de API do OpenWeatherMap da seguinte forma:
   ```env
   API_KEY=sua_chave_de_api_aqui
   ```
5. **Inicie o servidor Flask**:
   ```bash
   python app.py
   ```
6. Abra o navegador e acesse a aplicação em `http://127.0.0.1:5000`.
