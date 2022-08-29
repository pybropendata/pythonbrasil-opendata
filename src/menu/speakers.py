import pandas as pd
import streamlit as st

import util
from plot import CreatePlot


def write(year):

    util.write_header()
    st.markdown("---")
    util.write_title("- PALESTRAS")

    tickest_df = get_event_speakers(year)

    if tickest_df.empty:
        return None

    total = tickest_df.shape[0]
    st.markdown(f"## Tivemos um total de **{total}** ministrantes !!!")

    plot_who(tickest_df)


def get_event_speakers(year):
    data = util.get_df_from_csv("ministrantes-atividades", year)

    if not data:
        st.write(f"Sem dados para o ano de {year}")
        return pd.DataFrame()

    df = pd.read_csv(data)

    columns = ['Idioma', 'Pessoa com necessidades específicas:',
       'Se você marcou "Sim" na pergunta anterior, quais recursos de acessibilidade você vai precisar?',
       'Como você se identifica?',
       'Faz parte da população T (Pessoa Transgênera, Travesti)?',
       'Orientação sexual:', 'Como você se define?', 'Em qual UF você reside?',
       'Essa é a sua primeira vez participando da Python Brasil?',
       'Você já ministrou atividades em uma edição da Python Brasil?',
       'Se sim, em quais das edições?',
       'Já ministrou alguma atividade em algum outro evento?',
       'Se sim, sinalize abaixo: [Meetups e eventos locais]',
       'Se sim, sinalize abaixo: [Eventos com até 200 pessoas]',
       'Se sim, sinalize abaixo: [Eventos com até 1000 pessoas]',
       'Se sim, sinalize abaixo: [Eventos  com mais de 1000 pessoas]',
       'Se sim, sinalize abaixo: [Eventos internacionais]',
       'Se sim, sinalize abaixo: [Eventos online]', 'Você programa em Python?',
       'Essa palestra tem coautoria?', 'Nível do conteúdo:',
       'Escolha até 3 palavras chave. A primeira palavra chave deve representar a área que a sua palestra está inserida (Ex: Testes, IA, Pessoas, Carreira)',
       'Trilha']
       
    return df[columns].fillna("N/A")

def plot_who(df):
    columns_who = ['Idioma', 'Pessoa com necessidades específicas:',
       'Se você marcou "Sim" na pergunta anterior, quais recursos de acessibilidade você vai precisar?',
       'Como você se identifica?',
       'Faz parte da população T (Pessoa Transgênera, Travesti)?',
       'Orientação sexual:', 'Como você se define?',
       'Essa é a sua primeira vez participando da Python Brasil?',
       'Você já ministrou atividades em uma edição da Python Brasil?',
       'Se sim, em quais das edições?',
       'Já ministrou alguma atividade em algum outro evento?',
       'Se sim, sinalize abaixo: [Meetups e eventos locais]',
       'Se sim, sinalize abaixo: [Eventos com até 200 pessoas]',
       'Se sim, sinalize abaixo: [Eventos com até 1000 pessoas]',
       'Se sim, sinalize abaixo: [Eventos  com mais de 1000 pessoas]',
       'Se sim, sinalize abaixo: [Eventos internacionais]',
       'Se sim, sinalize abaixo: [Eventos online]', 'Você programa em Python?',
       'Essa palestra tem coautoria?', 'Nível do conteúdo:',
       'Escolha até 3 palavras chave. A primeira palavra chave deve representar a área que a sua palestra está inserida (Ex: Testes, IA, Pessoas, Carreira)',
       'Trilha']

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

    columns_where = ["Em qual UF você reside?"]

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



