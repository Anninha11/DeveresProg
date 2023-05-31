import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Análise de Arquivo CSV")
csv_file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])
if csv_file is not None:
    data = pd.read_csv(csv_file)
    st.write(data)
    st.subheader("Gráfico de Barras")
    fig, ax = plt.subplots()
    data.plot(kind="bar", ax=ax)
    st.pyplot(fig)
