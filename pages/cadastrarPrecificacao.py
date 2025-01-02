
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
from controller import precificacaoController as pr


st.title("Nova Precificação")

st.caption("Dados da precificação")


col1, col2 = st.columns(2)
with col1:
    contratante = st.text_input('Contratante')


col1, col2, col3 = st.columns(3)

with col1:
    vigencia = st.number_input('Vigencia:', 0)
with col2:
    dt_sessao = st.date_input('Data Sessão:')


col1, col2 = st.columns(2)
with col1:
    criterio_julgamento = st.text_input('Criterio Julgamento')
    modo_disputa = st.selectbox('Modo Disputa', ['Aberto', 'Fechado'])

    objeto = st.text_input('Objeto da contratação')

col1, col2 = st.columns(2)
with col1:
    uf = st.selectbox('UF', ['AL',
                                'MT',
                                'MS',
                                'RS',
                                'SC',
                                'MG',
                                'RN',
                                'SP',
                                'AC',
                                'GO',
                                'PA',
                                'SE',
                                'AM',
                                'CE',
                                'DF',
                                'ES',
                                'PB',
                                'RJ',
                                'RR',
                                'TO',
                                'BA',
                                'PI',
                                'MA',
                                'AP',
                                'PR',
                                'RO',
                                'PE'])


st.caption("Itens da precificação")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        item_ma = st.selectbox('Airtime', ['Mobile Priority - 50Gb Subscription'
                                , 'Mobile Priority - 1TB Subscription'
                                , 'Mobile Priority - 5TB Subscription'
                                ,'Priority - 40GB Subscription'
                                ,'Priority - 1TB Subscription'
                                ,'Priority - 2TB Subscription'
                                ,'Priority - 6TB Subscription'])
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ma= st.number_input('Quant. Pontos: ', 0)
        importacao_ma = 0
    with col2:
        valor_ma = st.number_input('Vr. Aritime: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ma = st.number_input('(%)AirTime: ', 0)
      
    col1, col2 = st.columns(2)
    with col1:
        item_ml = st.selectbox('Locação de Equipamento', ['Antena Starlink Flat High Performance'
                                               , 'Antena Starlink Standard'
                                               , 'Adaptador Ethernet'
                                               ,'Inversor 12 V'
                                               ,'Patch Cord'
                                               ,'Maleta de transporte'
                                               ,'Pulsar IO'
                                               ,'Sistema de monitoramento (Gerencia Pulsar)'])
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml =st.number_input('Quant. Antena: ', 0)
        importacao_ml = 0
    with col2:
        valor_ml = st.number_input('Vr. Antena: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml = st.number_input('(%)Antena: ', 0)

    item_ml_eth = st.checkbox('Adaptador Ethernet')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_eth =st.number_input('Quant. Adaptador Ethernet: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_eth = st.number_input('Vr. Adaptador Ethernet: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_eth = st.number_input('(%)Adaptador Ethernet: ', 0)

    item_ml_inv = st.checkbox('Inversor 12 V')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_inv =st.number_input('Quant. Inversor 12 V: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_inv = st.number_input('Vr. Inversor 12 V: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_inv = st.number_input('(%)Inversor 12 V: ', 0)

    item_ml_ptch = st.checkbox('Patch Cord')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_ptch =st.number_input('Quant. Patch Cord: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_ptch = st.number_input('Vr. Patch Cord: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_ptch = st.number_input('(%)Patch Cord: ', 0)

    item_ml_mala = st.checkbox('Maleta de transporte')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_mala =st.number_input('Quant. Maleta de transporte: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_mala = st.number_input('Vr. Maleta de transporte: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_mala = st.number_input('(%)Maleta de transporte: ', 0)

    item_ml_pio = st.checkbox('Pulsar IO')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_pio =st.number_input('Quant. Pulsar IO: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_pio = st.number_input('Vr. Pulsar IO: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_pio = st.number_input('(%)Pulsar IO: ', 0)
    
    item_ml_mon = st.checkbox('Sist. Monitoramento (Gerencia Pulsar)')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_mon =st.number_input('Quant. Sist. Monitoramento: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_mon = st.number_input('Vr. Sist. Monitoramento: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_mon = st.number_input('(%)Sist. Monitoramento: ', 0)
    
    item_mo = st.checkbox('Servico de operacao e manutencao')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        quantidade_mo = st.number_input('Quant. Operação: ', 0)
        importacao_mo = 0
    with col2:
        valor_mo = st.number_input('Vr. Operação: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_mo = st.number_input('(%))Operação: ', 0)


    item_mn = st.checkbox('Serviço de Instalação')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        quantidade_mn = st.number_input('Quant. Instalação: ', 0)
        importacao_mn = 0
    with col2:
        valor_mn = st.number_input('Vr. Instalação: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_mn = st.number_input('(%)Instalação: ', 0)


st.caption("Indexadores")

col1, col2, col3 = st.columns(3)


with st.container():
    with col1:
        idx_ctc_dolar_airtime = 0
        idx_oveheade = st.number_input('Tx. Oveheade:', 0.0, value=0.0, step=.05, format="%f")
        idx_percentual = 0
        premio_seguro = st.number_input('Premio Seguro:', 0.0, value=0.0, step=.05, format="%f")
    with col2:
        idx_ctc_dolar_antena = 0
        idx_tx_importacao = st.number_input('Tx. Importação:', 0.0, value=0.0, step=.05, format="%f")
        overhead = st.number_input('Overhead:', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        idx_custos_financeiros = st.number_input('Tx. Custos Financeiros:', 0.0, value=0.0, step=.05, format="%f")
        idx_comissao = st.number_input('Tx. Comissão:', 0.0, value=0.0, step=.05, format="%f")
        percentual_garantia = st.number_input('(%)Garantia:', 0.0, value=0.0, step=.05, format="%f")

if st.button('Grava'):
    if contratante == '' and quantidade_ma == 0 and quantidade_ml == 0:
         st.warning("Campos obrigatorios não preenchidos!")
    else:
        if 'df_precificacao' not in st.session_state:
            st.session_state.df_precificacao = pd.DataFrame(columns=['codigo','contratante','qnt','freq','vigencia','marcem_precentual','vlr_total','criterio_jugamento','data_sessao','modo_disputa','objetp','uf','idx_ctc_dolar_airtime','idx_ctc_dolar_antena','idx_custos_financeiros','idx_oveheade','idx_tx_importacao','idx_comissao','idx_percentual','overhead','percentual_garantia','premio_seguro'])
        precificacao_data = {'codigo':9,'contratante': contratante,'qnt':0,'freq':0,'vigencia':vigencia,'marcem_precentual':0,'vlr_total':0,'criterio_jugamento':criterio_julgamento,'data_sessao':dt_sessao,'modo_disputa':modo_disputa,'objetp':objeto,'uf':uf,'idx_ctc_dolar_airtime':idx_ctc_dolar_airtime,'idx_ctc_dolar_antena':idx_ctc_dolar_antena,'idx_custos_financeiros':idx_custos_financeiros,'idx_oveheade':idx_oveheade,'idx_tx_importacao':idx_tx_importacao,'idx_comissao':idx_comissao,'idx_percentual':idx_percentual,'overhead':overhead,'percentual_garantia':percentual_garantia,'premio_seguro':premio_seguro}
        df_precificacao = pd.DataFrame(precificacao_data,index=[0])
        st.session_state.df_precificacao = pd.concat([st.session_state.df_precificacao, df_precificacao],ignore_index=True)
        
        if 'df_ma' not in st.session_state:
            st.session_state.df_ma = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ma_data = {'codigo':99,'cod_item': item_ma, 'vlr_venda':valor_ma,'qnt': quantidade_ma, 'percentual_desconto': percentual_ma, 'importacao': importacao_ma}
        df_ma = pd.DataFrame(param_ma_data,index=[0])
        st.session_state.df_ma = pd.concat([st.session_state.df_ma, df_ma],ignore_index=True)

        if 'df_ml' not in st.session_state:
                st.session_state.df_ml = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_data = {'codigo':99,'cod_item': item_ml, 'vlr_venda':valor_ml,'qnt': quantidade_ml, 'percentual_desconto': percentual_ml, 'importacao': importacao_ml}
        df_ml = pd.DataFrame(param_ml_data,index=[0])
        st.session_state.df_ml = pd.concat([st.session_state.df_ml, df_ml],ignore_index=True)
        
        if 'df_mn' not in st.session_state:
            st.session_state.df_mn = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_mn_data = {'codigo':99,'cod_item': item_mn, 'vlr_venda':valor_mn,'qnt': quantidade_mn, 'percentual_desconto': percentual_mn, 'importacao': importacao_mn}
        df_mn = pd.DataFrame(param_mn_data,index=[0])
        st.session_state.df_mn = pd.concat([st.session_state.df_mn, df_mn],ignore_index=True)


        if 'df_mo' not in st.session_state:
            st.session_state.df_mo = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_mo_data = {'codigo':99,'cod_item': item_mo, 'vlr_venda':valor_mo,'qnt': quantidade_mo, 'percentual_desconto': percentual_mo, 'importacao': importacao_mo}
        df_mo = pd.DataFrame(param_mo_data,index=[0])
        st.session_state.df_mo = pd.concat([st.session_state.df_mo, df_ma],ignore_index=True)

        if 'df_ml_eth' not in st.session_state:
                st.session_state.df_ml_eth = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_eth_data = {'codigo':99,'cod_item': item_ml_eth, 'vlr_venda':valor_ml_eth,'qnt': quantidade_ml_eth, 'percentual_desconto': percentual_ml_eth, 'importacao': importacao_ml}
        df_ml_eth = pd.DataFrame(param_ml_eth_data,index=[0])
        st.session_state.df_ml_eth = pd.concat([st.session_state.df_ml_eth, df_ml_eth],ignore_index=True)

        if 'df_ml_inv' not in st.session_state:
                st.session_state.df_ml_inv = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_inv_data = {'codigo':99,'cod_item': item_ml_inv, 'vlr_venda':valor_ml_inv,'qnt': quantidade_ml_inv, 'percentual_desconto': percentual_ml_inv, 'importacao': 0}
        df_ml_inv = pd.DataFrame(param_ml_inv_data,index=[0])
        st.session_state.df_ml_inv = pd.concat([st.session_state.df_ml_inv, df_ml_inv],ignore_index=True)

        if 'df_ml_ptch' not in st.session_state:
                st.session_state.df_ml_ptch = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_ptch_data = {'codigo':99,'cod_item': item_ml_ptch, 'vlr_venda':valor_ml_ptch,'qnt': quantidade_ml_ptch, 'percentual_desconto': percentual_ml_ptch, 'importacao': 0}
        df_ml_ptch = pd.DataFrame(param_ml_ptch_data,index=[0])
        st.session_state.df_ml_ptch = pd.concat([st.session_state.df_ml_ptch, df_ml_ptch],ignore_index=True)

        if 'df_ml_mala' not in st.session_state:
                st.session_state.df_ml_mala = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_mala_data = {'codigo':99,'cod_item': item_ml_mala, 'vlr_venda':valor_ml_mala,'qnt': quantidade_ml_mala, 'percentual_desconto': percentual_ml_mala, 'importacao': 0}
        df_ml_mala = pd.DataFrame(param_ml_mala_data,index=[0])
        st.session_state.df_ml_mala = pd.concat([st.session_state.df_ml_mala, df_ml_mala],ignore_index=True)

        if 'df_ml_pio' not in st.session_state:
                st.session_state.df_ml_pio = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_pio_data = {'codigo':99,'cod_item': item_ml_pio, 'vlr_venda':valor_ml_pio,'qnt': quantidade_ml_pio, 'percentual_desconto': percentual_ml_pio, 'importacao': 0}
        df_ml_pio = pd.DataFrame(param_ml_pio_data,index=[0])
        st.session_state.df_ml_pio = pd.concat([st.session_state.df_ml_pio, df_ml_pio],ignore_index=True)

        if 'df_ml_mon' not in st.session_state:
                st.session_state.df_ml_mon = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_mon_data = {'codigo':99,'cod_item': item_ml_mon, 'vlr_venda':valor_ml_mon,'qnt': quantidade_ml_mon, 'percentual_desconto': percentual_ml_mon, 'importacao': 0}
        df_ml_mon = pd.DataFrame(param_ml_mon_data,index=[0])
        st.session_state.df_ml_mon = pd.concat([st.session_state.df_ml_mon, df_ml_mon],ignore_index=True)

        file_name_precificacao = 'precificacao/precificacao.csv'
        file_name_pram_item = 'param_itens/param_itens.csv'

        credential = au.getCredentialFromJson(controle.getServiceAccountFile())
        credentialBQ = au.getCredentialBigQuery(controle.getServiceAccountFile())
        cod_precificacao = controle.gravaPrecificacaoNaCamadaSilver(df_precificacao,credential,file_name_precificacao,credentialBQ)

        credential = au.getCredentialFromJson(controle.getServiceAccountFile())
        credentialBQ = au.getCredentialBigQuery(controle.getServiceAccountFile())
        controle.gravaItensPrecificacaoNaCamadaSilver(df_ma, df_ml,df_mn,df_mo,df_ml_eth,df_ml_inv,df_ml_mala,df_ml_mon,df_ml_pio,df_ml_ptch,credential,file_name_pram_item,credentialBQ)
        

        location_precificacao = 'gs://pulsar-transiente-zone/precificacao/precificacao.csv'
        table_precificacao = 'electric-armor-429218-g7.prf_cs.precificacao'

        location_param = 'gs://pulsar-transiente-zone/param_itens/param_itens.csv'
        table_param = 'electric-armor-429218-g7.prf_cs.param_itens'

        location_grp = 'gs://pulsar-transiente-zone/grp_itens_prf/grp_itens_prf.csv'
        table_grp = 'electric-armor-429218-g7.prf_cs.grp_itens_prf'

        location_log = 'gs://pulsar-transiente-zone/log_precificacao/log_precificacao.csv'
        table_log = 'electric-armor-429218-g7.prf_cs.log_precificacao'
        
        
        table_gold_precificacao = 'electric-armor-429218-g7.prf_cs.gold_dados_precificacao'
        table_gold_custos = 'electric-armor-429218-g7.prf_cs.gold_custos'
        table_gold_impostos = 'electric-armor-429218-g7.prf_cs.gold_impostos'
        table_silver_precificacao = 'electric-armor-429218-g7.prf_cs.vw_silver_dados_precificacao'
        table_silver_custos = 'electric-armor-429218-g7.prf_cs.vw_silver_custos'
        table_silver_impostos = 'electric-armor-429218-g7.prf_cs.vw_silver_impostos'
        file_name_precificacao = 'gold_dados_precificacao.csv'
        file_name_custos = 'gold_custos.csv'
        file_name_impostos = 'gold_impostos.csv'

        credentialBQ = au.getCredentialBigQuery(controle.getServiceAccountFile())
        credential = au.getCredentialFromJson(controle.getServiceAccountFile())
        controle.gravaDadosNaCamadaGold(table_gold_precificacao,table_silver_precificacao,file_name_precificacao,credential,credentialBQ)

        credentialBQ = au.getCredentialBigQuery(controle.getServiceAccountFile())
        credential = au.getCredentialFromJson(controle.getServiceAccountFile())
        controle.gravaDadosNaCamadaGold(table_gold_custos,table_silver_custos,file_name_custos,credential,credentialBQ)

        credentialBQ = au.getCredentialBigQuery(controle.getServiceAccountFile())
        credential = au.getCredentialFromJson(controle.getServiceAccountFile())
        controle.gravaDadosNaCamadaGold(table_gold_impostos,table_silver_impostos,file_name_impostos,credential,credentialBQ)

        
        df_precificacao_silver = pr.getDadosPrecificacaoSilverByCodigo(cod_precificacao)
        df_csto_silver = pr.getCustosSilverPrecificacao(cod_precificacao)
        df_impostos_silver = pr.getImpostosSilverPrecificacao(cod_precificacao)

        st.info("Dados gravados com sucesso!")

        df_precificacao_silver.contratante.iloc[0]
        
        with st.container():    
            df = pd.DataFrame(
                {
                    "categoria": df_precificacao_silver.categoria,
                    "vigencia": df_precificacao_silver.vigencia,
                    "desc_item": df_precificacao_silver.desc_item,
                    "qnt": df_precificacao_silver.qnt,
                    "valor_ponto": df_precificacao_silver.valor_ponto
                    
                }
            )
            st.dataframe(
                df,
                column_config={
                    "categoria": "categoria",
                    "vigencia": "vigencia",
                    "desc_item": "desc_item",
                    "qnt":"qnt",
                    "valor_ponto":"valor_ponto"
                },
                hide_index=True,
            )

            df_custos = pd.DataFrame(
                {
                    "custos": df_csto_silver.custos,
                    "vlr_custos": df_csto_silver.vlr_custos
                    
                }
            )
            st.dataframe(
                df_custos,
                column_config={
                    "custos": "custos",
                    "vlr_custos": "vlr_custos"
                },
                hide_index=True,
            )

            
            df_impostos = pd.DataFrame(
                {
                    "impostos": df_impostos_silver.imposto,
                    "vlr_impostos": df_impostos_silver.vlr_impostos
                    
                }
            )
            st.dataframe(
                df_impostos,
                column_config={
                    "impostos": "imposto",
                    "vlr_impostos": "vlr_impostos"
                },
                hide_index=True,
            )


st.link_button("Voltar", "/precificacao_app")



