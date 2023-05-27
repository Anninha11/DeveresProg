#Dever para o dia 30/05
import streamlit as st
import pandas as pd

def main():
    st.title("Visualização de arquivo CSV")
    file = st.file_uploader("ingrediente de comidas e alergias.csv")
    if file is not None:
        df = pd.read_csv(file)
        st.write(df)
if __name__ == "__main__":
    main()
