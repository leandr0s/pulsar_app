
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import graphviz
import pickle  # to load a saved modelimport base64  # to handle gif encoding

st.title("Nova Precificação")

st.caption("Dados da precificação")

st.text_area('Nome da precificação')
st.date_input('Data:')
st.number_input('Vigencia:', 0, 999)



st.caption("Itens da precificação")

with st.container():
    st.selectbox('Item: ', ['Apple', 'Banana', 'Orange'])
    st.number_input('Quantidade: ', 0, 10)
    st.number_input('Valor: ', 0, 999)


st.button('Gravar')
st.button('Cancelar')