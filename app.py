import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Este é meu primeiro streamlit!')
st.write('Streamlit é uma biblioteca Python de código aberto que permite a criação e o compartilhamento rápido de aplicativos da web personalizados para análise de dados e machine learning.')

data = {
    'Nome': ['Cauã', 'Júlio', 'Lara', 'Maria'],
    'Idade': ['23', '35', '45', '30'],
    'Salário': ['3000', '3500', '4000', '5000']
}

df = pd.DataFrame(data)
st.dataframe(df)

fig, ax = plt.subplots()
ax.bar(df['Nome'], df['Salário'])
st.pyplot(fig)