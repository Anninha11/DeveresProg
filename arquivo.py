import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('ingrediente de comidas e alergias.csv')
category_counts = data[['Food Product', 'Main Ingredient', 'Sweetener', 'Fat/Oil', 'Seasoning', 'Allergens', 'Prediction']].apply(pd.Series.value_counts)
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', subplots=True, layout=(4, 2), figsize=(10, 10), legend=False)
st.pyplot(plt)
