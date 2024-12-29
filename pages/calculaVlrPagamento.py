import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import controller.geraCamadaGold as controle
import bigframes.pandas as bf

from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.cloud import storage
from controller import precificacaoController as pr


st.title("Calcula o Valor de pagamento para a Precificação")

st.caption("Dados da precificação")

df_precificacao = pr.getPrecificacao('A',20)

col1, col2 = st.columns(2)
with col1:
    precificacao = st.selectbox('Selecione Precificação', df_precificacao.contratante)


if st.button('Calcula'):
    st.info("Dados gravados com sucesso!")