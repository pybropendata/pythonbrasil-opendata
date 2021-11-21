import pandas as pd
import streamlit as st
import util
from plot import CreatePlot


def write(year):

    util.write_header()
    st.markdown("---")
    util.write_title("- FEEDBACKS")

    feedbacks_df = get_event_feedbacks(year)

    if feedbacks_df.empty:
        st.write("EM DESENVOLVIMENTO")
        return None
        
    total = feedbacks_df.shape[0]
    st.markdown(
        f"## Tivemos um total de **{total}** respostas ao formulário de feedback!!!"
    )

    plot_who(feedbacks_df)


def get_event_feedbacks(year):
    data = util.get_df_from_csv("feedbacks",year)

    if not data:
        return pd.DataFrame();
        
    df = pd.read_csv(data, index_col=0).reset_index()

    df = df.fillna("N/A")

    return df


def plot_who(df):
    colunas_categoricas = [
        "Essa foi sua primeira Python Brasil?",
        "Avalie a sua satisfação em geral com... [Python Brasil 2020]",
        "Avalie a sua satisfação em geral com... [Rodas de conversa]",
        "Avalie a sua satisfação em geral com... [Palestras]",
        "Avalie a sua satisfação em geral com... [Keynotes]",
        "Avalie a sua satisfação em geral com... [Tutoriais]",
        "Avalie a sua satisfação em geral com... [Sprints]",
        "O que você achou dos... [Temas das palestras?]",
        "O que você achou dos... [Níveis das palestras?]",
        "O que você achou dos... [Temas dos tutoriais?]",
        "O que você achou dos... [Níveis dos tutoriais?]",
        "Qual a chance de você participar da Python Brasil 2021? [Se for online]",
        "Qual a chance de você participar da Python Brasil 2021? [Se for presencial]",
    ]
    colunas_multiplas = [
        "Quais atividades você participou?",
        "Quais dias você participou?",
        "Se a Python Brasil 2021 for presencial, qual seria o maior impeditivo para você participar do evento?",
    ]

    df_cat = df[colunas_categoricas].copy()
    df_multiplas = df[colunas_multiplas].copy()
    
    SHOWVALUES = ["Quantidade", "Percentual"]

    st.title("Visualizar Valores em:")
    show_values = st.radio("", SHOWVALUES)

    if show_values == "Quantidade":
        for item in df_cat.columns:
            st.markdown(f"**{item}**")
            simple_bar_chart = CreatePlot(sample_df=df_cat).categorical_count_bar_plot(
                item, percent=False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)

        for col in colunas_multiplas:
            st.markdown(f"**{col}**")
            df_plot = (
                df_multiplas[col]
                .str.split(",", expand=True)
                .stack()
                .reset_index(level=0)
                .set_index("level_0")
                .rename(columns={0: col})[[col]]
            )
            df_plot[col] = df_plot[col].str.strip()
            simple_bar_chart = CreatePlot(sample_df=df_plot).categorical_count_bar_plot(
                col, percent=False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for item in df_cat.columns:
            st.markdown(f"**{item}**")
            simple_bar_chart = CreatePlot(sample_df=df_cat).categorical_count_bar_plot(
                item, percent=True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)

        for col in colunas_multiplas:
            st.markdown(f"**{col}**")
            df_plot = (
                df_multiplas[col]
                .str.split(",", expand=True)
                .stack()
                .reset_index(level=0)
                .set_index("level_0")
                .rename(columns={0: col})[[col]]
            )
            df_plot[col] = df_plot[col].str.strip()
            simple_bar_chart = CreatePlot(sample_df=df_plot).categorical_count_bar_plot(
                col, percent=True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
