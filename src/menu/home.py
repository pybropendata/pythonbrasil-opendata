import streamlit as st

def main():
    st.header("Dados Abertos Python Brasil")
    st.caption("Projeto de dados abertos do evento Python Brasil")
    
    st.markdown(
        """
        Este é o projeto de dados abertos dos eventos da Python Brasil,tendo como base os dados de inscrições, acesso dos videos das lives do Youtube e dados de metricas dos servidor do Discord 
        utilizado durante o evento.
        A fonte de dados é o [repositório oficial de dados do evento](https://github.com/pythonbrasil/dados/blob/main/dados/README.md). 
        Todos os dados utilizados aqui foram a anonimizados, além disso os mesmos as análises devem respeitar tando o [código de conduta](https://python.org.br/cdc/) quando leis vigentes no Brasil. 
        """
    )
    st.subheader("Contribua")
    st.markdown(
        "Esse é um projeto de código aberto que aceita contribuições, comentários e ajuda são bem vindos. "
        "Você encontra o código fonte no seguinte repositório [pythonbrasil-opendata](https://github.com/pybropendata/pythonbrasil-opendata). "
        "Esse projeto também agradece a MarcSkovMadsen por manter o [awesome-streamlit](https://github.com/MarcSkovMadsen/awesome-streamlit). "
        "Algumas partes de códigos e dicas vem diretamente dessa excelente curadoria, recomendamos também contribuir com esse projeto. "
    )

    st.subheader("Deixe seu feedback")
    #sentiment_mapping = ["1", "2", "3", "4", "5"]
    #selected = st.feedback("stars")
    #if selected is not None:
    #    st.markdown(f"Você deu {sentiment_mapping[selected]} estrela(s).")

    with st.form("Diga o que você achou do projeto"):
        st.markdown("Como você avalia esse projeto?")
        st.feedback("stars")
        st.text_input(
            "✍🏻 Deixe seu comentário",             
            placeholder="Escreva aqui..."
        )

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Formulário enviado com sucesso!")
            #TODO: salvar o comentário em algum lugar (banco de dados, arquivo, etc.)