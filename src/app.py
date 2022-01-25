import streamlit as st

import pages.discord
import pages.feedbacks
import pages.home
import pages.py2020
import pages.py2021
import pages.speakers
import pages.talks
import pages.tutorials
import pages.youtube
import util


def main():

    EVENTS = {
        "Início": (pages.home,None),
        "Pyhton Brasil 2020": (pages.py2020,2020),
        "Pyhton Brasil 2021": (pages.py2021,2021),
    }

    PAGES = {
        "Palestras": pages.talks,
        "Tutoriais": pages.tutorials,
        "Ministrantes": pages.speakers,
        "Lives Youtube": pages.youtube,
        "Discord": pages.discord,
        "Feedback": pages.feedbacks,
    }

    st.sidebar.write()

    svg = util.svg_to_line("./assets/pylogo75.svg")
    st.sidebar.write(
        f"{util.parse_svg_html(svg)}",
        unsafe_allow_html=True,
    )

    st.sidebar.title("Visualizar dados do evento")
    event_select = st.sidebar.selectbox("", list(EVENTS.keys()))
    event = EVENTS[event_select]
    util.write_page(event[0])


    if event[0].has_ok:
        st.sidebar.title("Páginas")
        page_selection = st.sidebar.radio("", list(PAGES.keys()))
        page = PAGES[page_selection]
        with st.spinner(f"Carregando {page_selection} ..."):
            util.write_page(page,year=event[1])

    st.sidebar.title("Contribua")
    st.sidebar.info(
        "Esse é um projeto de código aberto que aceita contribuições, comentários e ajuda são bem vindos. "
        "Você encontra o código fonte no seguinte repositório [pythonbrasil-opendata](https://github.com/pybropendata/pythonbrasil-opendata). "
        "Esse projeto também agradece a MarcSkovMadsen por manter o [awesome-streamlit](https://github.com/MarcSkovMadsen/awesome-streamlit). "
        "Algumas partes de códigos e dicas vem diretamente dessa excelente curadoria, recomendamos também contribuir com esse projeto. "
    )
    st.sidebar.title("Sobre")
    st.sidebar.info(
        """
        Este é o projeto de dados abertos dos eventos da Python Brasil,tendo como base os dados de inscrições, acesso dos videos das lives do Youtube e dados de metricas dos servidor do Discord 
        utilizado durante o evento.
        A fonte de dados é o [repositório oficial de dados do evento](https://github.com/pythonbrasil/dados/blob/main/dados/README.md). 
        Todos os dados utilizados aqui foram a anonimizados, além disso os mesmos as análises devem respeitar tando o [código de conduta](https://python.org.br/cdc/) quando leis vigentes no Brasil. 
        """
    )


if __name__ == "__main__":
    main()
