import pandas as pd
import streamlit as st
import util
from plot import CreatePlot


def write():

    util.write_header()
    st.markdown("---")
    util.write_title("- LIVES YOUTUBE")

    lives_df = get_lives_tutorials()

    views = lives_df["Views"].sum()
    hours = round(lives_df["Watch time (hours)"].sum(), 2)
    days = round(lives_df["Watch time (days)"].sum(), 2)
    year = round(days / 365, 1)

    st.markdown(f"## - Tivemos um total de **{int(views)}** visualizações ")
    st.markdown(
        f"## - Com um total de  **{hours}** horas de visualizações, o  que dá **{days}** consecutivo assistindo tudo !!"
    )
    st.markdown(f"## **ISSO DÁ PRATICAMENTE {year} ANOS DE CONTÉUDO SEM PARAR !!!**")

    plot_youtube(lives_df)


def get_lives_tutorials():
    df = util.get_df_from_csv("youtube-videos")

    df["Tag"] = df["Video title"].str.split(" ").str[0].replace(" ", "")

    df["Watch time (hours)"] = df["Watch time (hours)"].round(decimals=2)

    df["Watch time (days)"] = (df["Watch time (hours)"] / 24).round(decimals=2)

    df.loc[
        df["Video title"]
        == "[PyBr2020] Trilha PEP0 - 2 -  Quinta-feira - Dia 05/11 #pybr2020",
        "Video title",
    ] = "[PyBr2020] Trilha PEP0 - Quinta-feira - Dia 05/11 #pybr2020"

    df.loc[
        df["Video title"]
        == "[PyBr2020] Trilha PEP0 - 2 - Quarta-feira  - Dia 04/11 #pybr2020",
        "Video title",
    ] = "[PyBr2020] Trilha PEP0 - Quarta-feira - Dia 04/11 #pybr2020"

    df.loc[
        df["Video title"]
        == "[PyBr2020] Trilha PEP404 - 2 - Quinta-feira - Dia 05/11 #pybr2020",
        "Video title",
    ] = "[PyBr2020] Trilha PEP404 - Quinta-feira - Dia 05/11 #pybr2020"

    df = df[df["Tag"] == "[PyBr2020]"][
        ["Video title", "Views", "Watch time (hours)", "Watch time (days)"]
    ].copy()

    return df.groupby(["Video title"]).sum().reset_index()


def plot_youtube(df):
    columns_who = ["Views", "Watch time (hours)", "Watch time (days)"]

    SHOWVALUES = ["Quantidade", "Percentual"]

    st.title("Visualizar Valores em:")
    show_values = st.radio("", SHOWVALUES)

    if show_values == "Quantidade":
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).value_count_bar_plot(
                total_column=items, categorical_column="Video title", percent=False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).value_count_bar_plot(
                total_column=items, categorical_column="Video title", percent=True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
