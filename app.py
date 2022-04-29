
import streamlit as st
import pandas as pd
import plotly.express as px

#  python -m pip install --upgrade pip

if __name__ == '__main__':

    st.title("Ciao Ragazzi Lezione finita")

    df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")

    st.dataframe(df)

    fig = px.line(df, x="data" , y=["terapia_intensiva","ricoverati_con_sintomi"])
    fig.update_layout(
        title="Plot",
        paper_bgcolor="grey",
        plot_bgcolor = "black",
        hovermode="x"
    )
    st.plotly_chart(fig)

    fig = px.line(df, x="data" , y=["totale_positivi","totale_casi"])
    st.plotly_chart(fig)

    btn_run = st.button("Run Model")
    if (btn_run==True):
        st.text("Button has been pressed")

    btn_clear = st.button("Clear Model")
    if (btn_clear==True):
        btn_run = False




