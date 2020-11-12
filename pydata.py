import streamlit as st
import scr.pybr2020
import scr.home

def main():
    PAGES = {
        "Home" :scr.home,
        "PyBr2020": scr.pybr2020,
    }    

    st.markdown(f"""
        # Site com os dados da Python Brasil
        ## Local para disponibizar o acesso dos dados publicos dos eventos 
    """)

    st.sidebar.markdown("**Selecione uma Python Brasil**")

    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        write_page(page)

def write_page(page):  # pylint: disable=redefined-outer-name
    """Writes the specified page/module
    Our multipage app is structured into sub-files with a `def write()` function
    Arguments:
        page {module} -- A module with a 'def write():' function
    """
    # _reload_module(page)
    page.write()

if __name__ == '__main__':
    main()