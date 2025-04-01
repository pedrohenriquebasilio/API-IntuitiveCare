API de Busca de Operadoras de Saúde

Uma API simples construída com FastAPI para buscar operadoras de saúde a partir de um arquivo CSV (operadoras_saude.csv). A API permite buscar operadoras por termos relacionados a razão social, nome fantasia, cidade ou UF, com um sistema básico de relevância.

Funcionalidades
- Rota GET /: Verifica se a API está funcionando.
- Rota POST /search: Busca operadoras com base em uma query e limite de resultados.

Pré-requisitos
- Python 3.8 ou superior
- Bibliotecas Python: fastapi, uvicorn, pandas, pydantic

Instalação
1. Clone o repositório (se aplicável) ou crie um diretório para o projeto:
   mkdir intuitiveCare
   cd intuitiveCare
2. Instale as dependências:
   Crie um ambiente virtual (opcional, mas recomendado) e instale os pacotes:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install fastapi uvicorn pandas pydantic
3. Coloque o arquivo CSV:
   Certifique-se de que o arquivo operadoras_saude.csv está no mesmo diretório que o script server.py.

Como Executar
1. Inicie o servidor:
   No diretório do projeto, execute:
   uvicorn server:app --reload
   - A API estará disponível em http://127.0.0.1:8000.
2. Verifique o funcionamento:
   Acesse http://127.0.0.1:8000/ no navegador ou via ferramenta como Postman para ver a mensagem:
   {"message": "API de Busca de Operadoras de Saúde está funcionando!"}

Uso da API
Rota GET /
- Método: GET
- URL: http://127.0.0.1:8000/
- Resposta:
  {"message": "API de Busca de Operadoras de Saúde está funcionando!"}
Rota POST /search
- Método: POST
- URL: http://127.0.0.1:8000/search
- Corpo da requisição (JSON):
  {
    "query": "sao paulo",
    "limit": 5
  }
- Resposta (exemplo):
  [
    {
      "Razao_Social": "OPERADORA SAO PAULO LTDA",
      "Nome_Fantasia": "Saúde SP",
      "Cidade": "São Paulo",
      "UF": "SP"
    }
  ]
- Notas:
  - Se query estiver vazia, retorna erro 400.
  - Se não houver resultados, retorna uma lista vazia [].

Testando com Postman
1. Importe a coleção API_Busca_Operadoras.postman_collection.json no Postman.
2. Configure as requisições:
   - GET /: Verifica a API.
   - POST /search: Testa diferentes queries e limites.
3. Execute os testes diretamente na interface do Postman.

Estrutura do Projeto
intuitiveCare/
├── server.py               # Código principal da API
├── operadoras_saude.csv    # Arquivo CSV com os dados
├── README.txt              # Este arquivo
└── IntuitiveCare.postman_collection       # coleção json
