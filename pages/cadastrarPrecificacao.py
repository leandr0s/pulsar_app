
import pandas as pd
import streamlit as st
import controller.geraCamadaGold as controle
from googleapiclient.discovery import build


st.title("Nova Precificação")

st.caption("Dados da precificação")


col1, col2 = st.columns(2)
with col1:
    contratante = st.text_input('Contratante')


col1, col2, col3 = st.columns(3)

with col1:
    vigencia = st.number_input('Vigência:', 0)
with col2:
    dt_sessao = st.date_input('Data Sessão:')


col1, col2 = st.columns(2)
with col1:
    criterio_julgamento = st.text_input('Criterio Julgamento')
    modo_disputa = st.selectbox('Modo Disputa', ['Aberto', 'Fechado'])

    objeto = st.text_input('Objeto da contratação')

col1, col2 = st.columns(2)
with col1:
    uf = st.selectbox('UF', ['AC',
                                'AL',
                                'AM',
                                'AP',
                                'BA',
                                'CE',
                                'DF',
                                'ES',
                                'GO',
                                'MA',
                                'MG',
                                'MS',
                                'MT',
                                'PA',
                                'PB',
                                'PE',
                                'PI',
                                'PR',
                                'RJ',
                                'RN',
                                'RO',
                                'RR',
                                'RS',
                                'SC',
                                'SE',
                                'SP',
                                'TO'])


st.caption("Itens da precificação")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        item_ma = st.selectbox('Airtime', ['Terminal Access (500GB)'
                                , 'Terminal Access (50GB)'])

        
    col1, col2, col3 = st.columns(3)

    with col1:
        franquia_ma = st.number_input('Franquia GB: ', 0)
        importacao_ma = 0
    with col2:
        quantidade_ma= st.number_input('Quant. Pontos: ', 0)
    with col3:
        valor_ma = st.number_input('Vr. Aritime: ', 0.0, value=0.0, step=.05, format="%f")
        percentual_ma = 0 #  st.number_input('(%)AirTime: ', 0)
      
    col1, col2 = st.columns(2)
    with col1:
        item_ml = st.selectbox('Locação de Equipamento', ['Antena Starlink Flat High Performance'
                                               , 'Antena Starlink Standard'])
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml =st.number_input('Quant. Antena: ', 0)
        importacao_ml = 0
    with col2:
        valor_ml = st.number_input('Vr. Antena: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml = 0 # st.number_input('(%)Antena: ', 0)

    item_ml_eth = st.checkbox('Adaptador Ethernet')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_eth =st.number_input('Quant. Adaptador Ethernet: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_eth = st.number_input('Vr. Adaptador Ethernet: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_eth = 0 # st.number_input('(%)Adaptador Ethernet: ', 0)

    item_ml_inv = st.checkbox('Inversor 12 V')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_inv =st.number_input('Quant. Inversor 12 V: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_inv = st.number_input('Vr. Inversor 12 V: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_inv = 0 #  st.number_input('(%)Inversor 12 V: ', 0)

    item_ml_ptch = st.checkbox('Patch Cord')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_ptch =st.number_input('Quant. Patch Cord: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_ptch = st.number_input('Vr. Patch Cord: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_ptch = 0 # st.number_input('(%)Patch Cord: ', 0)

    item_ml_mala = st.checkbox('Maleta de transporte')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_mala =st.number_input('Quant. Maleta de transporte: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_mala = st.number_input('Vr. Maleta de transporte: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_mala = 0 #  st.number_input('(%)Maleta de transporte: ', 0)

    item_ml_pio = st.checkbox('Pulsar IO')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_pio =st.number_input('Quant. Pulsar IO: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_pio = st.number_input('Vr. Pulsar IO: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_pio = 0 # st.number_input('(%)Pulsar IO: ', 0)
    
    item_ml_mon = st.checkbox('Sist. Monitoramento (Gerencia Pulsar)')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_mon =st.number_input('Quant. Sist. Monitoramento: ', 0)
        importacao_outros = 0
    with col2:
        valor_ml_mon = st.number_input('Vr. Sist. Monitoramento: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_ml_mon = 0 # st.number_input('(%)Sist. Monitoramento: ', 0)
    
    item_mo = st.checkbox('Serviço de operaçâo e manutenção')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        quantidade_mo = st.number_input('Quant. Operação: ', 0)
        importacao_mo = 0
    with col2:
        valor_mo = st.number_input('Vr. Operação: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_mo = 0 # st.number_input('(%))Operação: ', 0)


    item_mn = st.radio('Servico de Intalação', ['Sem Instalação','Eventual', 'Recorrente'])

    print(item_mn)    

    col1, col2, col3 = st.columns(3)
    
    with col1:
        quantidade_mn = st.number_input('Quant. Instalação: ', 0)
        importacao_mn = 0
    with col2:
        valor_mn = st.number_input('Vr. Instalação: ', 0.0, value=0.0, step=.05, format="%f")
    with col3:
        percentual_mn = 0 # st.number_input('(%)Instalação: ', 0)


st.caption("Indexadores")

col1, col2, col3 = st.columns(3)


with st.container():
    with col1:
        idx_ctc_dolar_airtime = 0
        idx_oveheade = st.number_input('Tx. Ovehead:', 0.0, value=7.0, step=.05, format="%f")
        idx_percentual = 0
        premio_seguro = st.number_input('Prêmio Seguro:', 0.0, value=2.5, step=.05, format="%f")
    with col2:
        idx_ctc_dolar_antena = 0
        idx_tx_importacao = st.number_input('Tx. Importação:', 0.0, value=0.0, step=.05, format="%f")
        percentual_garantia = st.number_input('(%)Garantia:', 0.0, value=5.0, step=.05, format="%f")
    with col3:
        idx_custos_financeiros = st.number_input('Tx. Custos Financeiros:', 0.0, value=3.0, step=.05, format="%f")
        idx_comissao = st.number_input('Tx. Comissão:', 0.0, value=1.5, step=.05, format="%f")
        overhead = idx_oveheade #st.number_input('Overhead:', 0.0, value=0.0, step=.05, format="%f")
        

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
        param_ma_data = {'codigo':99,'cod_item': item_ma, 'vlr_venda':valor_ma,'qnt': quantidade_ma, 'percentual_desconto': percentual_ma, 'importacao': importacao_ma, 'franquia':franquia_ma}
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
        st.session_state.df_mo = pd.concat([st.session_state.df_mo, df_mo],ignore_index=True)

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

        file_name_precificacao = '..\\app\\data\\precificacao.csv'
        file_name_pram_item = '..\\app\\data\\param_itens.csv'
        file_name_grp_itens_prf = "..\\app\\data\\grp_itens_prf.csv"
        file_name_itens_prf = "..\\app\\data\\dados_itens.csv"
        file_name_log_precificacao = '..\\app\\data\\log_precificacao.csv'
        file_name_data_log_precificacao = "..\\app\\data\\dados_log_precificacao.csv"

        df_log_precificacao = pd.read_csv(file_name_log_precificacao, sep=';')
        print(df_log_precificacao)
        cod_precificacao = controle.gravaPrecificacaoDataFile(df_precificacao,file_name_precificacao,df_log_precificacao.iloc[-1]['cod_precificacao']+1)
        controle.gravaItensPrecificacaoDataFile(df_ma, df_ml,df_mn,df_mo,df_ml_eth,df_ml_inv,df_ml_mala,df_ml_mon,df_ml_pio,df_ml_ptch,file_name_pram_item,cod_precificacao)

        print(df_precificacao)

        
        st.info("Dados gravados com sucesso!")

st.link_button("Voltar", "/precificacao_app")



