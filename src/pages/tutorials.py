import pandas as pd
import streamlit as st
import util
from plot import CreatePlot


def write(year):

    util.write_header()
    st.markdown("---")
    util.write_title("- TUTORIAIS")

    tutorials_df = get_event_tutorials(year)

    total = tutorials_df.shape[0]
    st.markdown(f"## Tivemos um total de **{total}** inscrições para os tutorias !!!")

    plot_who(tutorials_df)


def get_event_tutorials(year):
    df = util.get_df_from_csv("inscrições-tutoriais",year)
    rename_columns = {
        "Orientação sexual:": "Orientação sexual",
        "Se outro, qual?": "Se define - Se outro, qual?",
        "Se outro, qual?.1": "Se identifica - Se outro, qual?",
        "Se outro, qual?.2": "Orientação sexual - Se outro, qual?",
        "Se sim, qual?": "Necessidades específicas - Se sim, qual?",
        "Faz parte da população T (pessoa transgênera, travesti)? ": "Faz parte da população T (pessoa transgênera, travesti)?",
    }

    return (
        df[
            [
                "Como você se define?",
                "Se outro, qual?",
                "Como você se identifica?",
                "Se outro, qual?.1",
                "Faz parte da população T (pessoa transgênera, travesti)? ",
                "Orientação sexual:",
                "Se outro, qual?.2",
                "Pessoa com necessidades específicas?",
                "Se sim, qual?",
            ]
        ]
        .rename(columns=rename_columns)
        .fillna("N/A")
    )


def plot_who(df):
    columns_who = [
        "Como você se define?",
        "Se define - Se outro, qual?",
        "Como você se identifica?",
        "Se identifica - Se outro, qual?",
        "Faz parte da população T (pessoa transgênera, travesti)?",
        "Orientação sexual",
        #'Orientação sexual - Se outro, qual?',
        "Pessoa com necessidades específicas?",
        "Necessidades específicas - Se sim, qual?",
    ]

    SHOWVALUES = ["Quantidade", "Percentual"]

    st.title("Visualizar Valores em:")
    show_values = st.radio("", SHOWVALUES)

    if show_values == "Quantidade":
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items, percent=False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items, percent=True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
