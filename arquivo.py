import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
st.title("Análise de Arquivo CSV")
csv_file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])
if csv_file is not None:
    data = pd.read_csv(csv_file)
    st.write(data)
    numeric_columns = data.select_dtypes(include='number')
    if not numeric_columns.empty:
        st.subheader("Gráfico de Barras")
        fig, ax = plt.subplots()
        numeric_columns.plot(kind="bar", ax=ax)
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        st.image(buffer, caption='Gráfico de Barras', use_column_width=True)
    else:
        st.write("Não há colunas numéricas no arquivo CSV.")
