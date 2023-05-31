install matplotlib.pyplot
install streamlit
install pandas
install matplotlib

import matplotlib.pyplot as plt
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
data = pd.read_csv('ingrediente de comidas e alergias.csv')
category_counts = data[['Food Product', 'Main Ingredient', 'Sweetener', 'Fat/Oil', 'Seasoning', 'Allergens', 'Prediction']].apply(pd.Series.value_counts)
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', subplots=True, layout=(4, 2), figsize=(10, 10), legend=False)
st.pyplot(plt)
