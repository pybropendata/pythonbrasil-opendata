
import streamlit as st
import pandas as pd

from lib.plot import CreatePlot

def write():
    st.write("___________________________________")

    st.markdown("""
    ## DADOS DA PYTHON BRASIL 2020!! ##
    """)

    plot_data(get_inscrições())

def get_inscrições():
    return pd.read_csv('./public_data/2020-11-10-pybr2020-inscricoes.csv')

def plot_data(df):

    select_column = st.selectbox(
        "Selecione uma coluna para ver a distribução",
        df.columns
    )  

    simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot(select_column)
    st.plotly_chart(simple_bar_chart, use_container_width=True)

    hist_chart = CreatePlot(sample_df=df).histogram_plot(x_column=select_column)
    st.plotly_chart(hist_chart,use_container_width=True)

    
    