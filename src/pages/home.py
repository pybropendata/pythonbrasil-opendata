import streamlit as st
import util

has_ok=False
def write():
    util.write_title("- Python Brasil")
    st.text("")
    util.render_img("./assets/PyBrOpenData-alternativa.png", "Python Brasil Open Data")
    st.text("") 
