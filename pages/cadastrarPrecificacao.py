
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt


st.title("Nova Precificação")

st.caption("Dados da precificação")


col1, col2 = st.columns(2)
with col1:
    st.text_area('Contratrante')


col1, col2, col3 = st.columns(3)

with col1:
    st.number_input('Vigencia:', 0, 999)
with col2:
    st.number_input('Margem Percentual:', 0.0, 999.9, value=0.0, step=.05, format="%f")
with col3:
    st.date_input('Data Sessão:')



col1, col2 = st.columns(2)
with col1:
    st.text_area('Criterio Julgamento')
    st.selectbox('Modo Disputa', ['Aberto', 'Fechado', 'Outros'])

    st.text_area('Objeto')

col1, col2 = st.columns(2)
with col1:
    st.selectbox('UF', ['BA', 'MG', 'RJ'])


st.caption("Itens da precificação")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox('Airtime_MA', ['Mobile Priority - 50Gb Subscription'
                                , 'Mobile Priority - 1TB Subscription'
                                , 'Mobile Priority - 5TB Subscription'
                                ,'Priority - 40GB Subscription'
                                ,'Priority - 1TB Subscription'
                                ,'Priority - 2TB Subscription'
                                ,'Priority - 6TB Subscription'])
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.number_input('Quantidade_MA: ', 0, 10)
        st.number_input('importacao_MA: ', 0, 999)
    with col2:
        st.number_input('Valor Venda_MA: ', 0.0, 999.9, value=0.0, step=.05, format="%f")
    with col3:
        st.number_input('percentual Desconto_MA: ', 0, 999)
      
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox('Locação de Equipamento_ML', ['Antena Starlink Flat High Performance'
                                               , 'Antena Starlink Standard'
                                               , 'Adaptador Ethernet'
                                               ,'Inversor 12 V'
                                               ,'Patch Cord'
                                               ,'Maleta de transporte'
                                               ,'Pulsar IO'
                                               ,'Sistema de monitoramento (Gerencia Pulsar)'])
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.number_input('Quantidade_ML: ', 0, 10)
        st.number_input('importacao_ML: ', 0, 999)
    with col2:
        st.number_input('Valor Venda_ML: ', 0.0, 999.9, value=0.0, step=.05, format="%f")
    with col3:
        st.number_input('percentual Desconto_ML: ', 0, 999)

    st.checkbox('Servico de operacao e manutencao')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.number_input('Quantidade_MO: ', 0, 10)
        st.number_input('importacao_MO: ', 0, 999)
    with col2:
        st.number_input('Valor Venda_MO: ', 0.0, 999.9, value=0.0, step=.05, format="%f")
    with col3:
        st.number_input('percentual Desconto_MO: ', 0, 999)


    st.checkbox('Serviço de Instalação')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.number_input('Quantidade_MN: ', 0, 10)
        st.number_input('importacao_MN: ', 0, 999)
    with col2:
        st.number_input('Valor Venda_MN: ', 0.0, 999.9, value=0.0, step=.05, format="%f")
    with col3:
        st.number_input('percentual Desconto_MN: ', 0, 999)


col1, col2, col3 = st.columns(3)

with col1:
    st.number_input('idx_ctc_dolar_airtime:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    st.number_input('idx_oveheade:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    st.number_input('idx_percentual:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    st.number_input('premio_seguro:', 0.0, 999.9, value=0.0, step=.05, format="%f")
with col2:
    st.number_input('idx_ctc_dolar_antena:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    st.number_input('idx_tx_importacao:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    st.number_input('overhead:', 0.0, 999.9, value=0.0, step=.05, format="%f")
with col3:
    st.number_input('idx_custos_financeiros:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    st.number_input('idx_comissao:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    st.number_input('percentual_garantia:', 0.0, 999.9, value=0.0, step=.05, format="%f")

if st.button('Gravar'):
    st.info("It's easy to build a Streamlit app")
st.button('Cancelar')