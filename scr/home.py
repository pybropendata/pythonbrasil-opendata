
import streamlit as st
import base64

def write():

    f = open("./assets/site-logo.svg","r")
    lines = f.readlines()
    line_string=''.join(lines)

    render_svg(line_string)

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)
