# Projeto Dados Abertos Python Brasil

Esse projeto tem como objetivo disponibilizar dados abertos referentes ao evento Python Brasil, utilizando a plataforma Streamlit para visualização e análise dos dados.

Neste repositório, você encontrará scripts para baixar, processar e visualizar os dados relacionados ao evento Python Brasil, incluindo informações sobre participantes, palestras e tutoriais. Utilizamos dados disponibilizados no repositório oficial de dados abertos do Python Brasil e oferecemos uma interface amigável para explorar essas informações.

No aplicativo Streamlit desenvolvido a partir deste repositório, trazemos os dados das seguintes edições:

- Python Brasil 2020 | Evento online devido à pandemia
- Python Brasil 2021 | Evento online devido à pandemia

## Requisitos

- Python 3.8 ou superior
- _Streamlit_
- _Pandas_
- _Requests_
- _Plotly_

## Como executar

1. Clone este repositório

    ```bash
    git clone https://github.com/seu_usuario/pythonbrasil-opendata.git

    cd pythonbrasil-opendata
    ```

2. Crie um ambiente virtual

    ```bash
    python -m venv .venv
    ```

3. Ative o ambiente virtual

    ```bash
    source venv/bin/activate  # Para Linux/Mac
    venv/Scripts/activate  # Para Windows
    ```

4. Instale as dependências

    ```bash
    pip install -r requirements.txt
    ```

5. Execute o app streamlit

    ```bash
    streamlit run src/app.py
    ```

## Agradecimento

Esse projeto agradece ao https://awesome-streamlit.org/ curadoria de exemplos e soluções do streamlit, muita soluções organizada pelos mesmos estão sendo utilizadas aqui.
