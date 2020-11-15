import pandas as pd
import streamlit as st
import util
from plot import CreatePlot
from datetime import datetime


def write():

    util.write_header()
    st.markdown("---")
    util.write_title("- DISCORD")

    discord_text_df = get_discord_text()
    discord_voice_df = get_discord_voice()

    messages = discord_text_df["messages"].sum()
    minutes  = round(discord_voice_df["speaking_minutes"].sum(),2)
    hours = round(minutes/60, 2)
    days = round(hours/24, 2)
    year = round(days / 365, 1)

    st.markdown(f"## - No Discord tivemos um total de **{(messages)}** enviadas ")
    st.markdown(f"## - Além disso, nas messas de bar e canais de áudios tivemos **{(minutes)} minutos** de conversas ")
    st.markdown(f"## - Com um total de  **{hours} horas** de áudios, o que dá **{days} dias** consecutivo ouvindo tudo !!")

    plot_discord(discord_text_df,discord_voice_df)


def get_discord_text():
    df = util.get_df_from_csv("discord-atividade-por-texto").reset_index()

    df['date'] = pd.to_datetime(df['interval_start_timestamp']).dt.tz_convert(tz='America/Sao_Paulo').dt.date

    return df[df['date'] >= datetime(2018, 11, 2).date()][['date','messages']]

def get_discord_voice():
    df = util.get_df_from_csv("discord-atividade-por-voz").reset_index()

    df['date'] = pd.to_datetime(df['interval_start_timestamp']).dt.tz_convert(tz='America/Sao_Paulo').dt.date
    
    return df[df['date'] >= datetime(2018, 11, 2).date()][['date','speaking_minutes']]

def plot_discord(df_text,df_audio):
    SHOWVALUES = ["Quantidade", "Percentual"]

    st.title("Visualizar Valores em:")
    show_values = st.radio("", SHOWVALUES)

    plot_discord_text(df_text,show_values)
    plot_discord_voice(df_audio,show_values)

def plot_discord_text(df,show_values):
    columns_who = ["messages"]

    if show_values == "Quantidade":
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).value_count_bar_plot(
                total_column=items, categorical_column="date", percent=False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).value_count_bar_plot(
                total_column=items, categorical_column="date", percent=True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)

def plot_discord_voice(df,show_values):
    columns_who = ["speaking_minutes"]

    if show_values == "Quantidade":
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).value_count_bar_plot(
                total_column=items, categorical_column="date", percent=False
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)
    else:
        for items in df[columns_who].columns:
            st.markdown(f"**{items}**")

            simple_bar_chart = CreatePlot(sample_df=df).value_count_bar_plot(
                total_column=items, categorical_column="date", percent=True
            )
            st.plotly_chart(simple_bar_chart, use_container_width=True)