
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt


st.title("Nova Precificação")

st.caption("Dados da precificação")

st.text_area('Contratrante')
st.number_input('Vigencia:', 0, 999)
st.number_input('Margem Percentual:', 0, 999)
st.text_area('Criterio Julgamento')
st.date_input('Data Sessão:')
st.selectbox('Modo Disputa', ['Aberto', 'Fechado', 'Outros'])
st.text_area('Objeto')
st.selectbox('UF', ['BA', 'MG', 'RJ'])
st.number_input('idx_ctc_dolar_airtime:', 0, 999)
st.number_input('idx_ctc_dolar_antena:', 0, 999)
st.number_input('idx_custos_financeiros:', 0, 999)
st.number_input('idx_oveheade:', 0, 999)
st.number_input('idx_tx_importacao:', 0, 999)
st.number_input('idx_comissao:', 0, 999)
st.number_input('idx_percentual:', 0, 999)
st.number_input('overhead:', 0, 999)
st.number_input('percentual_garantia:', 0, 999)
st.number_input('premio_seguro:', 0, 999)




st.caption("Itens da precificação")

with st.container():
    st.selectbox('Airtime_MA', ['Mobile Priority - 50Gb Subscription'
                                , 'Mobile Priority - 1TB Subscription'
                                , 'Mobile Priority - 5TB Subscription'
                                ,'Priority - 40GB Subscription'
                                ,'Priority - 1TB Subscription'
                                ,'Priority - 2TB Subscription'
                                ,'Priority - 6TB Subscription'])
    st.number_input('Quantidade_MA: ', 0, 10)
    st.number_input('Valor Venda_MA: ', 0, 999)
    st.number_input('percentual Desconto_MA: ', 0, 999)
    st.number_input('importacao_MA: ', 0, 999)

    st.selectbox('Locação de Equipamento_ML', ['Antena Starlink Flat High Performance'
                                               , 'Antena Starlink Standard'
                                               , 'Adaptador Ethernet'
                                               ,'Inversor 12 V'
                                               ,'Patch Cord'
                                               ,'Maleta de transporte'
                                               ,'Pulsar IO'
                                               ,'Sistema de monitoramento (Gerencia Pulsar)'])
    st.number_input('Quantidade_ML: ', 0, 10)
    st.number_input('Valor Venda_ML: ', 0, 999)
    st.number_input('percentual Desconto_ML: ', 0, 999)
    st.number_input('importacao_ML: ', 0, 999)

    st.selectbox('Serviço de Disponibilidade_MO', ['Servico de operacao e manutencao'])
    st.number_input('Quantidade_MO: ', 0, 10)
    st.number_input('Valor Venda_MO: ', 0, 999)
    st.number_input('percentual Desconto_MO: ', 0, 999)
    st.number_input('importacao_MO: ', 0, 999)

    st.selectbox('Serviço de Implantação_MN', ['Instalação'])
    st.number_input('Quantidade_MN: ', 0, 10)
    st.number_input('Valor Venda_MN: ', 0, 999)
    st.number_input('percentual Desconto_MN: ', 0, 999)
    st.number_input('importacao_MN: ', 0, 999)


st.button('Gravar')
st.button('Cancelar')