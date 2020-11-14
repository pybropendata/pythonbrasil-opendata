import pandas as pd
import streamlit as st
import util
from plot import CreatePlot


def write():
    st.markdown("---")
    util.write_title("- INSCRIÇÕES")

    tickest_df = get_event_tickets()

    OPTIONS = ["Inscrições","Quem","Onde","Python"]

    st.sidebar.title("Dados de Inscrições do Evento")
    select_column = st.sidebar.selectbox("", OPTIONS)
    
    if select_column == "Quem":
        st.markdown(f"## Detalhes sobre as Quem")
        plot_who(tickest_df)
    elif select_column == "Onde":
        st.markdown(f"## Detalhes sobre as Onde")
        plot_where(tickest_df)
    elif select_column == "Python":
        st.markdown(f"## Detalhes sobre as Python")
        plot_python(tickest_df)
    elif select_column == "Inscrições":
        total = tickest_df.shape[0] 
        st.markdown(f"## Tivemos um total de **{total}** inscrições para o evento !!!")
        st.markdown(f"## Selecione alguma opção na barra lateral em:")
        st.markdown(f"## `Dados de Inscrições do Evento` para ver detalhes.")
    else:
        st.write("Escolha uma opção")

def get_event_tickets():
    df = util.get_df_from_csv("inscrições-palestras")

    rename_columns = {
        "Orientação sexual:":"Orientação sexual",
        "Se outro, qual?":"Se define - Se outro, qual?",
        "Se outro, qual?.1": "Se identifica - Se outro, qual?",
        "Se outro, qual?.2": "Orientação sexual - Se outro, qual?",
        "Se sim, qual?": "Necessidades específicas - Se sim, qual?",
        "Se sim, qual?.1": "comunidade local - Se sim, qual?",
    }

    return df[
        [
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
    ].rename(columns=rename_columns).fillna('N/A')

def plot_who(df):
    columns_who = ['Como você se define', 'Se define - Se outro, qual?',
        'Como você se identifica?', 'Se identifica - Se outro, qual?',
        'Faz parte da população T (pessoa transgênera, travesti)?',
        'Orientação sexual', 'Orientação sexual - Se outro, qual?',
        'Pessoa com necessidades específicas?',
        'Necessidades específicas - Se sim, qual?']

    SHOWVALUES = ["Quantidade","Percentual"]

    st.title("Visualizar Valores em:")
    show_values = st.radio("", SHOWVALUES)

    if show_values=="Quantidade":
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items,
                percent= False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items,
                percent= True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)


def plot_where(df):
    columns_where = ['Em qual UF você reside?','Em qual país você reside?']

    SHOWVALUES = ["Quantidade","Percentual"]

    st.title("Visualizar Valores em:")
    show_values = st.radio("", SHOWVALUES)

    if show_values=="Quantidade":
        for items in df[columns_where].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items,
                percent= False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for items in df[columns_where].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items,
                percent= True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)


def plot_python(df):
    columns_python = ['De quais edições da Python Brasil você já participou?',
        'Você já participou de algum outro evento Python?',
        'Você participou de outros eventos online durante a pandemia de covid-19?',
        'Há quanto tempo você programa em Python?',
        'Como você classificaria seu nível de conhecimento em Python?',
        'Você é estudante?', 'Você trabalha com Python?',
        'Você pretende submeter alguma atividades (palestra, tutorial) para a Python Brasil?',
        'Você faz parte de alguma comunidade local? (grupy, PUG, PyLadies, AfroPython)',
        'comunidade local - Se sim, qual?']

    SHOWVALUES = ["Quantidade","Percentual"]

    st.title("Visualizar Valores em:")
    show_values = st.radio("", SHOWVALUES)

    if show_values=="Quantidade":
        for items in df[columns_python].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items,
                percent= False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for items in df[columns_python].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items,
                percent= True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)




