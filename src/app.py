import streamlit as st
import streamlit_antd_components as sac

from menu import (home, py2020)

st.set_page_config(
    page_title="Python Brasil",
    page_icon="🐍",
    layout="wide",
    menu_items={"Report a bug": "https://github.com/pybropendata/pythonbrasil-opendata/issues"},
)

def main():

    # Exibe uma mensagem de boas-vindas ao usuário na barra lateral
    st.sidebar.image("./assets/PyBrOpenData-alternativa.png")
    st.sidebar.markdown("**.Dados Abertos Python Brasil.**", unsafe_allow_html=True)
    # Adiciona uma divisória na barra lateral
    st.sidebar.divider()

    with st.sidebar:
        pagina_selecionada = sac.menu([
            sac.MenuItem("Início", icon="house-fill"),
            sac.MenuItem('Edições', icon='box-fill', children=[
                    sac.MenuItem("PyBr 2020",icon="chevron-right"),
                    #sac.MenuItem("PyBr 2021",icon="chevron-right"),
                    #sac.MenuItem("PyBr 2022",icon="chevron-right"),
                    #sac.MenuItem("PyBr 2023",icon="chevron-right"),
                    #sac.MenuItem("PyBr 2024",icon="chevron-right"),
                ]),
            sac.MenuItem(type='divider'),
            sac.MenuItem('github', icon='github', href="https://github.com/pybropendata/pythonbrasil-opendata")
            ], open_all=True)

    page_mapping = {
        "Início": home.main,
        "Edições": py2020.main,
        "PyBr 2020": py2020.main
    }
    
    page_mapping[pagina_selecionada]()


if __name__ == "__main__":
    main()