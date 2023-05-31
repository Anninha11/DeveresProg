import streamlit as st
import pandas as pd
st.title("Análise de Arquivo CSV")
csv_file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])
if csv_file is not None:
    data = pd.read_csv(csv_file)
    st.write(data)
else:
    st.write("Nenhum arquivo selecionado.")
