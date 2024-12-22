
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import controller.geraCamadaGold as controle
import bigframes.pandas as bf
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.cloud import storage
from controller import auth2 as au


st.title("Nova Precificação")

st.caption("Dados da precificação")


col1, col2 = st.columns(2)
with col1:
    contratante = st.text_area('Contratrante')


col1, col2, col3 = st.columns(3)

with col1:
    vigencia = st.number_input('Vigencia:', 0, 999)
with col2:
    margem_percentual = st.number_input('Margem Percentual:', 0.0, 999.9, value=0.0, step=.05, format="%f")
with col3:
    dt_sessao = st.date_input('Data Sessão:')



col1, col2 = st.columns(2)
with col1:
    criterio_julgamento = st.text_area('Criterio Julgamento')
    modo_disputa = st.selectbox('Modo Disputa', ['Aberto', 'Fechado', 'Outros'])

    objeto = st.text_area('Objeto')

col1, col2 = st.columns(2)
with col1:
    uf = st.selectbox('UF', ['BA', 'MG', 'RJ'])


st.caption("Itens da precificação")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        item = st.selectbox('Airtime_MA', ['Mobile Priority - 50Gb Subscription'
                                , 'Mobile Priority - 1TB Subscription'
                                , 'Mobile Priority - 5TB Subscription'
                                ,'Priority - 40GB Subscription'
                                ,'Priority - 1TB Subscription'
                                ,'Priority - 2TB Subscription'
                                ,'Priority - 6TB Subscription'])
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade= st.number_input('Quantidade_MA: ', 0, 10)
        importacao = st.number_input('importacao_MA: ', 0, 999)
    with col2:
        valor = st.number_input('Valor Venda_MA: ', 0.0, 999.9, value=0.0, step=.05, format="%f")
    with col3:
        percentual = st.number_input('percentual Desconto_MA: ', 0, 999)
      
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
    idx_ctc_dolar_airtime = st.number_input('idx_ctc_dolar_airtime:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    idx_oveheade = st.number_input('idx_oveheade:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    idx_percentual = st.number_input('idx_percentual:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    premio_seguro = st.number_input('premio_seguro:', 0.0, 999.9, value=0.0, step=.05, format="%f")
with col2:
    idx_ctc_dolar_antena = st.number_input('idx_ctc_dolar_antena:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    idx_tx_importacao = st.number_input('idx_tx_importacao:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    overhead = st.number_input('overhead:', 0.0, 999.9, value=0.0, step=.05, format="%f")
with col3:
    idx_custos_financeiros = st.number_input('idx_custos_financeiros:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    idx_comissao = st.number_input('idx_comissao:', 0.0, 999.9, value=0.0, step=.05, format="%f")
    percentual_garantia = st.number_input('percentual_garantia:', 0.0, 999.9, value=0.0, step=.05, format="%f")

if st.button('Simulacão'):
    if 'df_precificacao' not in st.session_state:
        st.session_state.df_precificacao = pd.DataFrame(columns=['codigo','contratrante','qnt','freq','vigencia','marcem_precentual','vlr_total','criterio_jugamento','data_sessao','modo_disputa','objetp','uf','idx_ctc_dolar_airtime','idx_ctc_dolar_antena','idx_custos_financeiros','idx_oveheade','idx_tx_importacao','idx_comissao','idx_percentual','overhead','percentual_garantia','premio_seguro'])
    precificacao_data = {'codigo':9,'contratrante': contratante,'qnt':0,'freq':0,'vigencia':vigencia,'marcem_precentual':margem_percentual,'vlr_total':0,'criterio_jugamento':criterio_julgamento,'data_sessao':dt_sessao,'modo_disputa':modo_disputa,'objetp':objeto,'uf':uf,'idx_ctc_dolar_airtime':idx_ctc_dolar_airtime,'idx_ctc_dolar_antena':idx_ctc_dolar_antena,'idx_custos_financeiros':idx_custos_financeiros,'idx_oveheade':idx_oveheade,'idx_tx_importacao':idx_tx_importacao,'idx_comissao':idx_comissao,'idx_percentual':idx_percentual,'overhead':overhead,'percentual_garantia':percentual_garantia,'premio_seguro':premio_seguro}
    df_precificacao = pd.DataFrame(precificacao_data,index=[0])
    st.session_state.df_precificacao = pd.concat([st.session_state.df_precificacao, df_precificacao],ignore_index=True)
    
    if 'df_param_itens' not in st.session_state:
        st.session_state.df_param_itens = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
    param_itens_data = {'codigo':99,'cod_item': item, 'vlr_venda':valor,'qtd': quantidade, 'percentual_desconto': percentual, 'importacao': importacao}
    df_param_itens = pd.DataFrame(param_itens_data,index=[0])
    st.session_state.df_param_itens = pd.concat([st.session_state.df_param_itens, df_param_itens],ignore_index=True)

    file_name_precificacao = 'precificacao99.csv'
    file_name_pram_item = 'param_itens99.csv'
    file_name_log = 'log_precificacao99.csv'
    file_name_grp_itens = 'grp_itens_prf99.csv'
    credential = au.getCredentialFromJson(controle.getServiceAccountFile())
    controle.gravaDadosNaCamadaSilver(df_precificacao,credential,file_name_precificacao)
    controle.gravaDadosNaCamadaSilver(df_param_itens,credential,file_name_pram_item)
    #controle.gravaDadosNaCamadaSilver(df_grp,credential,file_name_grp_itens)
    #controle.gravaDadosNaCamadaSilver(df_log,credential,file_name_log)
    st.info("Simulacao realizada com sucesso!")
    
if st.button('Grava'):
    table_name_precificacao = 'prf_cs.gold_dados_precificacao'
    table_name_custos = 'prf_cs.vw_silver_custos'
    table_name_impostos = 'prf_cs.vw_silver_impostos'
    controle.gravaDadosNaCamadaGold(table_name_precificacao)
    controle.gravaDadosNaCamadaGold(table_name_custos)
    controle.gravaDadosNaCamadaGold(table_name_impostos)
    
    #au.get_data_table("electric-armor-429218-g7","electric-armor-429218-g7.prf_cs.log_precificacao", "us-east4",[])
    st.info("Dados gravados com sucesso!")
st.button('Cancelar')