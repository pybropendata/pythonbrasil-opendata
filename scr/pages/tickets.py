import pandas as pd
import streamlit as st
import util
from plot import CreatePlot


def write():
    st.markdown("---")

    st.markdown(
        """
    ## Dados sobre as inscrições e tutoriais 
    """
    )

    plot_data(get_event_tickets())


def get_event_tickets():
    df = util.get_df_from_csv("inscrições-palestras")

    rename_columns = {
        "Se outro, qual?": "Se define - Se outro, qual?",
        "Se outro, qual?.1": "Se identifica - Se outro, qual?.",
        "Se outro, qual?.2": "Orientação sexual - Se outro, qual?",
        "Se sim, qual?": "Necessidades específicas - Se sim, qual?",
        "Se sim, qual?.1": "comunidade local - Se sim, qual?",
    }

    return df[
        [
            "Quantidade",
            "Tipo de ingresso",
            "Status do participante",
            "Como você se define",
            "Se outro, qual?",
            "Como você se identifica?",
            "Se outro, qual?.1",
            "Faz parte da população T (pessoa transgênera, travesti)?",
            "Orientação sexual:",
            "Se outro, qual?.2",
            "Pessoa com necessidades específicas?",
            "Se sim, qual?",
            "Em qual UF você reside?",
            "Em qual país você reside?",
            "De quais edições da Python Brasil você já participou?",
            "Você já participou de algum outro evento Python?",
            "Você participou de outros eventos online durante a pandemia de covid-19?",
            "Há quanto tempo você programa em Python?",
            "Como você classificaria seu nível de conhecimento em Python?",
            "Você é estudante?",
            "Você trabalha com Python?",
            "Você pretende submeter alguma atividades (palestra, tutorial) para a Python Brasil?",
            "Você faz parte de alguma comunidade local? (grupy, PUG, PyLadies, AfroPython)",
            "Se sim, qual?.1",
        ]
    ].rename(columns=rename_columns)


def plot_data(df):

    select_column = st.selectbox(
        "Selecione uma coluna para ver a distribução", df.columns
    )

    simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
        select_column
    )
    st.plotly_chart(simple_bar_chart, use_container_width=True)

    # hist_chart = CreatePlot(sample_df=df).histogram_plot(x_column=select_column)
    # st.plotly_chart(hist_chart, use_container_width=True)
