import base64
import os

import pandas as pd
import requests
import streamlit as st
from PIL import Image


def get_df_from_csv(csv_name):
    return pd.read_csv(download_csv_file(csv_name), index_col=0)


def download_csv_file(csv_name):
    req = requests.get(
        f"https://raw.githubusercontent.com/pythonbrasil/dados/main/dados/python-brasil-2020/{csv_name}.csv"
    )

    if not os.path.exists("./files"):
        os.makedirs("./files")
    csv_name = f"./files/{csv_name}.csv"
    url_content = req.content
    with open(csv_name, "wb") as csv_file:
        csv_file.write(url_content)
    csv_file.close()
    return csv_name


def write_page(page):
    """Writes the specified page/module
    Our multipage app is structured into sub-files with a `def write()` function
    Arguments:
        page {module} -- A module with a 'def write():' function
    """
    # _reload_module(page)
    page.write()


def write_header():
    svg = svg_to_line("./assets/pylogo_50.svg")
    st.write(
        f"{parse_svg_html(svg)} **Python Brasil 2021 - Dados Abertos**",
        unsafe_allow_html=True,
    )


def write_title(body: str):
    """Uses st.write to write the title as f'Awesome Streamlit {body}'
    - plus the awesome badge
    - plus a link to the awesome-streamlit GitHub page
    Arguments:
        body {str} -- [description]
    """
    st.write(f"# PyBR2021 - Dados Abertos {body} ")


def parse_svg_html(svg):
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    return r'<img src="data:image/svg+xml;base64,%s"/>' % b64


def render_svg(svg):
    """Renders the given svg string."""
    st.write(parse_svg_html(svg), unsafe_allow_html=True)


def svg_to_line(svg_file):
    f = open(svg_file, "r")
    lines = f.readlines()
    line_string = "".join(lines)
    return line_string


def render_svg_file(svg_file):
    render_svg(svg_to_line(svg_file))


def render_img(img_file):
    image = Image.open(img_file)
    st.image(
        image, caption="Logo colorido da Python Brasil 2021", use_column_width=True
    )
