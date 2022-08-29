import pandas as pd
import streamlit as st

import util
from plot import CreatePlot


def write(year):

    util.write_header()
    st.markdown("---")
    util.write_title("- PALESTRAS")

    tickest_df = get_event_tickets(year)

    if tickest_df.empty:
        return None

    col = "Em qual país você reside?"
    tickest_df[col] = tickest_df[col].str.strip()
    tickest_df.loc[
        tickest_df[col]
        == "Por favor, que formulário mais sem sentido. Querem também saber que orientação sexual vou querer ter na próxima encarnação? Isso não tem sentido.",
        col,
    ] = "N/A"
    tickest_df.loc[tickest_df[col] == ",", col] = "N/A"
    tickest_df.loc[tickest_df[col] == "PNR", col] = "N/A"
    tickest_df.loc[tickest_df[col] == "Prefiro não responder.", col] = "N/A"
    tickest_df.loc[tickest_df[col] == "Alemanha, Berlin", col] = "Alemanha"
    tickest_df.loc[tickest_df[col] == "Canada", col] = "Canadá"
    tickest_df.loc[tickest_df[col] == "Dublin, Irlanda", col] = "Irlanda"
    tickest_df.loc[tickest_df[col] == "Ireland", col] = "Irlanda"
    tickest_df.loc[tickest_df[col] == "irlanda", col] = "Irlanda"
    tickest_df.loc[tickest_df[col] == "Italy", col] = "Itália"
    tickest_df.loc[tickest_df[col] == "Mocambique", col] = "Moçambique"
    tickest_df.loc[tickest_df[col] == "Países Baixo", col] = "Países Baixos"
    tickest_df.loc[tickest_df[col] == "Perú", col] = "Peru"
    tickest_df.loc[tickest_df[col] == "US", col] = "EUA"
    tickest_df.loc[tickest_df[col] == "USA", col] = "EUA"
    tickest_df.loc[tickest_df[col] == "Usa", col] = "EUA"
    tickest_df.loc[tickest_df[col] == "Estados Unidos", col] = "EUA"
    tickest_df.loc[tickest_df[col] == "United States", col] = "EUA"
    tickest_df.loc[tickest_df[col] == "CZ", col] = "República Tcheca"
    tickest_df.loc[tickest_df[col] == "United Kingdom", col] = "Reino Unido"
    tickest_df.loc[tickest_df[col] == "colombia", col] = "Colombia"
    tickest_df.loc[tickest_df[col] == "portugal", col] = "Portugal"
    tickest_df.loc[tickest_df[col] == "PT", col] = "Portugal"
    tickest_df.loc[tickest_df[col] == "thailand", col] = "Tailandia"
    tickest_df.loc[tickest_df[col] == "France", col] = "França"
    tickest_df.loc[tickest_df[col] == "Japao", col] = "Japão"

    OPTIONS = ["Inscrições", "Quem", "Onde", "Python"]

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


def get_event_tickets(year):
    data = util.get_df_from_csv("inscrições-palestras", year)

    if not data:
        st.write("EM DESENVOLVIMENTO")
        return pd.DataFrame()

    df = pd.read_csv(data)

    if year == 2020:
        rename_columns = {
            "Orientação sexual:": "Orientação sexual",
            "Se outro, qual?": "Se define - Se outro, qual?",
            "Se outro, qual?.1": "Se identifica - Se outro, qual?",
            "Se outro, qual?.2": "Orientação sexual - Se outro, qual?",
            "Se sim, qual?": "Necessidades específicas - Se sim, qual?",
            "Se sim, qual?.1": "Comunidade local - Se sim, qual?",
        }

        return (
            df[
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
                    "Você faz parte de alguma comunidade local? (grupy, PUG, PyLadies, AfroPython)",
                    "Se sim, qual?.1",
                ]
            ]
            .rename(columns=rename_columns)
            .fillna("N/A")
        )
    else:
        rename_columns = {
                "como_voce_se_define": "Como você se define",
                "como_voce_se_define_se_outro": "Se outro, qual?",
                "como_voce_se_indentifica": "Como você se identifica?",
                "como_voce_se_indentifica_se_outro": "Se define - Se outro, qual?",
                "faz_parte_da_populacao_t": "Faz parte da população T (pessoa transgênera, travesti)?",
                "orientaca_sexual": "Orientação sexual",
                "orientaca_sexual_se_outro": "Se identifica - Se outro, qual?",
                "pessoa_com_necessidade_especifica":"Pessoa com necessidades específicas?",
                "pessoa_com_necessidade_especifica_se_sim_qual":"Necessidades específicas - Se sim, qual?",
                "uf": "Em qual UF você reside?",
                "pais": "Em qual país você reside?",
                "edicoes_anteriores_pybr": "De quais edições da Python Brasil você já participou?",
                "eventos_pybr": "Você já participou de algum outro evento Python?",
                "eventos_online": "Você participou de outros eventos online durante a pandemia de covid-19?",
                "programa_em_python": "Há quanto tempo você programa em Python?",
                "nivel_python": "Como você classificaria seu nível de conhecimento em Python?",
                "estudante": "Você é estudante?",
                "trabalha_com_python": "Você trabalha com Python?",
                "parte_de_alguma_comunidade": "Você faz parte de alguma comunidade local? (grupy, PUG, PyLadies, AfroPython)",
                "comunidade_qual":"Comunidade local - Se sim, qual?"
            }
        return df.rename(columns=rename_columns).fillna("N/A")

def plot_who(df):
    columns_who = [
        "Como você se define",
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


def plot_where(df):
    columns_where = ["Em qual UF você reside?", "Em qual país você reside?"]

    SHOWVALUES = ["Quantidade", "Percentual"]

    st.title("Visualizar Valores em:")
    show_values = st.radio("", SHOWVALUES)

    if show_values == "Quantidade":
        for items in df[columns_where].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items, percent=False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for items in df[columns_where].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items, percent=True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)


def plot_python(df):
    columns_python = [
        "De quais edições da Python Brasil você já participou?",
        "Você já participou de algum outro evento Python?",
        "Você participou de outros eventos online durante a pandemia de covid-19?",
        "Há quanto tempo você programa em Python?",
        "Como você classificaria seu nível de conhecimento em Python?",
        "Você é estudante?",
        "Você trabalha com Python?",
        "Você faz parte de alguma comunidade local? (grupy, PUG, PyLadies, AfroPython)",
        "Comunidade local - Se sim, qual?",
    ]

    SHOWVALUES = ["Quantidade", "Percentual"]

    st.title("Visualizar Valores em:")
    show_values = st.radio("", SHOWVALUES)

    if show_values == "Quantidade":
        for items in df[columns_python].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items, percent=False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for items in df[columns_python].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(
                items, percent=True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
