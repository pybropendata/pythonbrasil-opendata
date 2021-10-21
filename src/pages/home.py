import streamlit as st

import util


def write():
    util.write_title("- PyBR2020 - ")
    st.text("")
    util.render_img("./assets/logo_colorido.png", "2020")
    st.text("")
    util.write_title("- PyBR2021 - ")
    util.render_img("./assets/pybr2021-ABREVIADO.png", "2021")
