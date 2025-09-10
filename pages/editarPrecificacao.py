import pandas as pd
import streamlit as st
import controller.geraCamadaGold as controle

from controller import precificacaoController as pr


st.title("Editar Precificação")

st.caption("Selecione a precificação")

df_selecao = pr.getPrecificacao('A',20)



col1, col2 = st.columns(2)
with col1:
    #contratante = None
    contratante = st.selectbox('Selecione Precificação', df_selecao.contratante, key="codigo")

if contratante != None:
    st.caption("Dados da precificação")
    pre_edit = pr.getDadosPrecificacao('A',contratante)
   

    col1, col2, col3 = st.columns(3)

    with col1:
        vigencia_pre = 0
        dt_sessao_pre = 0
        criterio_julgamento_pre = 0
        modo_disputa_pre = 'Selecione'
        objeto_pre = 0
        uf_pre = 'Selecione'

        if pre_edit.size > 0:
            vigencia_pre = pre_edit['vigencia'].iloc[0]
            dt_sessao_pre = pre_edit['data_sessao'].iloc[0]
            criterio_julgamento_pre = pre_edit['criterio_jugamento'].iloc[0]
            modo_disputa_pre = pre_edit.modo_disputa.iloc[0]
            objeto_pre = pre_edit['objetp'].iloc[0]
            uf_pre = pre_edit['uf'].iloc[0]
       
        vigencia = st.number_input('Vigência:', value=vigencia_pre)
    with col2:
        dt_sessao = st.text_input('Data Sessão:',value=dt_sessao_pre)

    col1, col2 = st.columns(2)
    with col1:
        criterio_julgamento = st.text_input('Criterio Julgamento',value=criterio_julgamento_pre)
        modo_disputa = st.selectbox('Modo Disputa', ['Aberto', 'Fechado'],placeholder=modo_disputa_pre)

        objeto = st.text_input('Objeto da contratação',value=objeto_pre)



    col1, col2 = st.columns(2)
    col1, col2 = st.columns(2)
    with col1:
        UF = {'AC':0, 'AL':1, 'AM':2,'AP':3, 'BA':4, 'CE':5, 'DF':6, 'ES':7, 'GO':8, 'MA':9, 'MG':10, 'MS':11, 'MT':12, 'PA':13, 'PB':14, 'PE':15, 'PI':16, 'PR':17, 'RJ':18, 'RN':19, 'RO':20, 'RR':21, 'RS':22, 'SC':23, 'SE':24, 'SP':25,'TO':26}
        uf = uf = st.selectbox('UF', ['AC',
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
                                'TO'],index=UF[uf_pre])


    st.caption("Itens da precificação")

    with st.container():
        col1, col2 = st.columns(2)
    with col1:
        item_ma_edit = pre_edit[pre_edit.grp_categoria == 'Subotal Serviço Airtime']
        cod_item_ma = 0
        cod_param_item_ma = 0
        qnt_ma_edit = 0
        vlr_venda_ma_edit = 0.0
        paconte_ma_edit = 0
        objeto_ma_edit = 'Selecione'
                
        if item_ma_edit.size > 0:
            cod_item_ma = item_ma_edit.cod_item.iloc[0]
            qnt_ma_edit = item_ma_edit.qnt.iloc[0]
            vlr_venda_ma_edit = item_ma_edit.vlr_venda.iloc[0]
            paconte_ma_edit = item_ma_edit.pacote.iloc[0]
            objeto_ma_edit = item_ma_edit.objeto.iloc[0]
            cod_param_item_ma = item_ma_edit['cod_param_item'].iloc[0]

        AIRTIME = {'Selecione':0,'Terminal Access (500GB)':1, 'Terminal Access (50GB)':2, 'Terminal Access (1GB)':3}
        item_ma = st.selectbox('Airtime', ['Selecione','Terminal Access (500GB)'
                                , 'Terminal Access (50GB)', 'Terminal Access (1GB)'], index=AIRTIME[objeto_ma_edit])

        
    col1, col2, col3 = st.columns(3)

    with col1:
        franquia_ma = st.number_input('Franquia GB: ', value=paconte_ma_edit, disabled=False)
        importacao_ma = 0
    with col2:
        quantidade_ma= st.number_input('Quant. Pontos: ', value=qnt_ma_edit, disabled=False)
    with col3:
        valor_ma = st.number_input('Vr. Aritime: ', step=.05, format="%f", value=vlr_venda_ma_edit, disabled=False)
        percentual_ma = 0 #  st.number_input('(%)AirTime: ', 0)
    
    col1, col2 = st.columns(2)
    with col1:
        item_ml_edit = pre_edit[pre_edit.grp_categoria == 'Subotal Antena Starlink Standard']
        cod_item_ml = 0
        cod_param_item_ml = 0
        qnt_ml_edit = 0
        vlr_venda_ml_edit = 0.0
        objeto_ml_edit = 'Selecione'
        
        if item_ml_edit.size > 0:
            cod_item_ml = item_ml_edit.cod_item.iloc[0]
            qnt_ml_edit = item_ml_edit.qnt.iloc[0]
            vlr_venda_ml_edit = item_ml_edit.vlr_venda.iloc[0]
            objeto_ml_edit = item_ml_edit.objeto.iloc[0]
            cod_param_item_ml = item_ml_edit['cod_param_item'].iloc[0]

        LOCACAO = {'Selecione':0,'Antena Starlink Flat High Performance':1, 'Antena Starlink Standard':2}
            
        item_ml = item_ml = st.selectbox('Locação de Equipamento', ['Selecione','Antena Starlink Flat High Performance'
                                               , 'Antena Starlink Standard'],index=LOCACAO[objeto_ml_edit])
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml = st.number_input('Quant. Antena: ', value=qnt_ml_edit, disabled=False)
        importacao_ml = 0
    with col2:
        valor_ml = st.number_input('Vr. Antena: ', step=.05, format="%f", value=vlr_venda_ml_edit, disabled=False) 
    with col3:
        percentual_ml = 0 # st.number_input('(%)Antena: ', 0)

    item_ml_eth_edit = pre_edit[pre_edit.cod_item == 10]
    cod_item_eth = 10
    cod_param_item_ml_eth = 0
    qnt_ml_eth_edit = 0
    vlr_venda_ml_eth_edit = 0.0
    objeto_ml_eth_edit = False
    if item_ml_edit.size > 0:
        cod_item_eth = item_ml_edit.cod_item.iloc[0]
        qnt_ml_eth_edit = item_ml_edit.qnt.iloc[0]
        vlr_venda_ml_eth_edit = item_ml_edit.vlr_venda.iloc[0]
        objeto_ml_eth_edit = True    
        cod_param_item_ml_eth = item_ml_edit['cod_param_item'].iloc[0]

    item_ml_eth = st.checkbox('Adaptador Ethernet',value=objeto_ml_eth_edit)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_eth =st.number_input('Quant. Adaptador Ethernet: ',value=qnt_ml_eth_edit)
        importacao_outros = 0
    with col2:
        valor_ml_eth = st.number_input('Vr. Adaptador Ethernet: ',value=vlr_venda_ml_eth_edit, step=.05, format="%f")
    with col3:
        percentual_ml_eth = 0 # st.number_input('(%)Adaptador Ethernet: ', 0)

    item_ml_inv_edit = pre_edit[pre_edit.cod_item == 11]
    cod_item_inv = 11
    cod_param_item_ml_inv = 0
    qnt_ml_inv_edit = 0
    vlr_venda_ml_inv_edit = 0.0
    objeto_ml_inv_edit = False
    if item_ml_inv_edit.size > 0:
        cod_item_inv = item_ml_inv_edit.cod_item.iloc[0]
        qnt_ml_inv_edit = item_ml_inv_edit.qnt.iloc[0]
        vlr_venda_ml_inv_edit = item_ml_inv_edit.vlr_venda.iloc[0]
        objeto_ml_inv_edit = True
        cod_param_item_ml_inv = item_ml_inv_edit['cod_param_item'].iloc[0]

    item_ml_inv = st.checkbox('Inversor 12 V',value=objeto_ml_inv_edit)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_inv =st.number_input('Quant. Inversor 12 V: ',value=qnt_ml_inv_edit)
        importacao_outros = 0
    with col2:
        valor_ml_inv = st.number_input('Vr. Inversor 12 V: ',value=vlr_venda_ml_inv_edit, step=.05, format="%f")
    with col3:
        percentual_ml_inv = 0 #  st.number_input('(%)Inversor 12 V: ', 0)

    item_ml_ptch_edit = pre_edit[pre_edit.cod_item == 12]
    cod_item_ptch = 12
    cod_param_item_ml_ptch = 0 
    qnt_ml_ptch_edit = 0
    vlr_venda_ml_ptch_edit = 0.0
    objeto_ml_ptch_edit = False
    if item_ml_ptch_edit.size > 0:
        cod_item_ptch = item_ml_ptch_edit.cod_item.iloc[0]
        qnt_ml_ptch_edit = item_ml_ptch_edit.qnt.iloc[0]
        vlr_venda_ml_ptch_edit = item_ml_ptch_edit.vlr_venda.iloc[0]
        objeto_ml_ptch_edit = True
        cod_param_item_ml_ptch = item_ml_ptch_edit['cod_param_item'].iloc[0]

    item_ml_ptch = st.checkbox('Patch Cord',value=objeto_ml_ptch_edit)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_ptch =st.number_input('Quant. Patch Cord: ',value=qnt_ml_ptch_edit)
        importacao_outros = 0
    with col2:
        valor_ml_ptch = st.number_input('Vr. Patch Cord: ',value=vlr_venda_ml_ptch_edit, step=.05, format="%f")
    with col3:
        percentual_ml_ptch = 0 # st.number_input('(%)Patch Cord: ', 0)

    item_ml_mala_edit = pre_edit[pre_edit.cod_item == 13]
    cod_item_mala = 13
    cod_param_item_ml_mala = 0
    qnt_ml_mala_edit = 0
    vlr_venda_ml_mala_edit = 0.0
    objeto_ml_mala_edit = False
    if item_ml_mala_edit.size > 0:
        cod_item_mala = item_ml_mala_edit.cod_item.iloc[0]
        qnt_ml_mala_edit = item_ml_mala_edit.qnt.iloc[0]
        vlr_venda_ml_mala_edit = item_ml_mala_edit.vlr_venda.iloc[0]
        objeto_ml_mala_edit = True
        cod_param_item_ml_mala = item_ml_mala_edit['cod_param_item'].iloc[0]

    item_ml_mala = st.checkbox('Maleta de transporte',value=objeto_ml_mala_edit)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_mala =st.number_input('Quant. Maleta de transporte: ',value=qnt_ml_mala_edit)
        importacao_outros = 0
    with col2:
        valor_ml_mala = st.number_input('Vr. Maleta de transporte: ',value=vlr_venda_ml_mala_edit, step=.05, format="%f")
    with col3:
        percentual_ml_mala = 0 #  st.number_input('(%)Maleta de transporte: ', 0)

    cod_item_pio = 14
    cod_param_item_ml_pio = 0
    item_ml_pio_edit = pre_edit[pre_edit.cod_item == cod_item_pio]
    qnt_ml_pio_edit = 0
    vlr_venda_ml_pio_edit = 0.0
    objeto_ml_pio_edit = False
    if item_ml_pio_edit.size > 0:
        cod_item_pio = item_ml_pio_edit.cod_item.iloc[0]
        qnt_ml_pio_edit = item_ml_pio_edit.qnt.iloc[0]
        vlr_venda_ml_pio_edit = item_ml_pio_edit.vlr_venda.iloc[0]
        objeto_ml_pio_edit = True
        cod_param_item_ml_pio = item_ml_pio_edit['cod_param_item'].iloc[0]

    item_ml_pio = st.checkbox('Pulsar IO',value=objeto_ml_pio_edit)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_pio =st.number_input('Quant. Pulsar IO: ',value=qnt_ml_pio_edit)
        importacao_outros = 0
    with col2:
        valor_ml_pio = st.number_input('Vr. Pulsar IO: ',value=vlr_venda_ml_pio_edit, step=.05, format="%f")
    with col3:
        percentual_ml_pio = 0 # st.number_input('(%)Pulsar IO: ', 0)

    cod_item_mon = 18
    item_mon_edit = pre_edit[pre_edit.cod_item == cod_item_mon]
    cod_param_item_ml_mon = 0
    qnt_ml_mon_edit = 0
    vlr_venda_ml_mon_edit = 0.0
    objeto_ml_mon_edit = False
    if item_mon_edit.size > 0:
        cod_item_mon = item_mon_edit.cod_item.iloc[0]
        qnt_ml_mon_edit = item_mon_edit.qnt.iloc[0]
        vlr_venda_ml_mon_edit = item_mon_edit.vlr_venda.iloc[0]
        objeto_ml_mon_edit = True
        cod_param_item_ml_mon = item_mon_edit['cod_param_item'].iloc[0]

    item_ml_mon = st.checkbox('Sist. Monitoramento (Gerencia Pulsar)',value=objeto_ml_mon_edit)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        quantidade_ml_mon =st.number_input('Quant. Sist. Monitoramento: ',value=qnt_ml_mon_edit)
        importacao_outros = 0
    with col2:
        valor_ml_mon = st.number_input('Vr. Sist. Monitoramento: ',value=vlr_venda_ml_mon_edit, step=.05, format="%f")
    with col3:
        percentual_ml_mon = 0 # st.number_input('(%)Sist. Monitoramento: ', 0)

    cod_item_mo = 17
    item_mo_edit = pre_edit[pre_edit.cod_item == cod_item_mo]
    cod_param_item_ml_mo = 0
    qnt_ml_mo_edit = 0
    vlr_venda_ml_mo_edit = 0.0
    objeto_ml_mo_edit = False
    if item_mo_edit.size > 0:
        cod_item_mo = item_mo_edit.cod_item.iloc[0]
        qnt_ml_mo_edit = item_mo_edit.qnt.iloc[0]
        vlr_venda_ml_mo_edit = item_mo_edit.vlr_venda.iloc[0]
        objeto_ml_mo_edit = True
        cod_param_item_ml_mo = item_mo_edit['cod_param_item'].iloc[0]
    
    item_mo = st.checkbox('Serviço de operaçâo e manutenção',value=objeto_ml_mo_edit)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        quantidade_mo = st.number_input('Quant. Operação: ',value=qnt_ml_mo_edit)
        importacao_mo = 0
    with col2:
        valor_mo = st.number_input('Vr. Operação: ',value=vlr_venda_ml_mo_edit, step=.05, format="%f")
    with col3:
        percentual_mo = 0 # st.number_input('(%))Operação: ', 0)
    cod_item_mn = 16
    item_mn_edit = pre_edit[pre_edit.cod_item == cod_item_mn]
    qnt_mn_edit = 0
    cod_param_item_mn = 0
    vlr_venda_mn_edit = 0.0
    objeto_mn_edit = 'Sem Instalação'
    if item_mn_edit.size > 0:
        cod_item_mn = item_mn_edit.cod_item.iloc[0]
        qnt_mn_edit = item_mn_edit.qnt.iloc[0]
        vlr_venda_mn_edit = item_mn_edit.vlr_venda.iloc[0]
        objeto_mn_edit = item_mn_edit.objeto.iloc[0]
        cod_param_item_mn = item_mn_edit['cod_param_item'].iloc[0]
    
    INSTALACAO = {'Sem Instalação':0, 'Instalacao':1, 'Instalacao Recorrente':2}

    item_mn = st.radio('Servico de Intalação', ['Sem Instalação','Eventual', 'Recorrente'],index=INSTALACAO[objeto_mn_edit], horizontal=True, label_visibility="collapsed")


    col1, col2, col3 = st.columns(3)
    
    with col1:
        quantidade_mn = st.number_input('Quant. Instalação: ',value=qnt_mn_edit)
        importacao_mn = 0
    with col2:
        valor_mn = st.number_input('Vr. Instalação: ',value=vlr_venda_mn_edit, step=.05, format="%f")
    with col3:
        percentual_mn = 0 # st.number_input('(%)Instalação: ', 0)

    st.caption("Indexadores")

    col1, col2, col3 = st.columns(3)


    with st.container():
        with col1:
            idx_ctc_dolar_airtime = 0
            idx_oveheade = st.number_input('Tx. Ovehead:', step=.05, format="%f",value=pre_edit['idx_oveheade'].iloc[0], disabled=False)
            idx_percentual = 0
            premio_seguro = st.number_input('Prêmio Seguro:', step=.05, format="%f",value=pre_edit['premio_seguro'].iloc[0], disabled=False)
        with col2:
            idx_ctc_dolar_antena = 0
            idx_tx_importacao = st.number_input('Tx. Importação:',step=.05, format="%f",value=pre_edit['idx_tx_importacao'].iloc[0], disabled=False)
            percentual_garantia = st.number_input('(%)Garantia:',  step=.05, format="%f",value=pre_edit['percentual_garantia'].iloc[0], disabled=False)
        with col3:
            idx_custos_financeiros = st.number_input('Tx. Custos Financeiros:', step=.05, format="%f",value=pre_edit['idx_custos_financeiros'].iloc[0], disabled=False)
            idx_comissao = st.number_input('Tx. Comissão:',step=.05, format="%f",value=pre_edit['idx_comissao'].iloc[0], disabled=False)
            overhead = idx_oveheade #st.number_input('Overhead:', 0.0, value=0.0, step=.05, format="%f")

if st.button('Gravar'):

    if contratante == '' and quantidade_ma == 0 and quantidade_ml == 0:
         st.warning("Campos obrigatorios não preenchidos!")
    else:
        if 'df_precificacao' not in st.session_state:
            st.session_state.df_precificacao = pd.DataFrame(columns=['codigo','contratante','qnt','freq','vigencia','marcem_precentual','vlr_total','criterio_jugamento','data_sessao','modo_disputa','objetp','uf','idx_ctc_dolar_airtime','idx_ctc_dolar_antena','idx_custos_financeiros','idx_oveheade','idx_tx_importacao','idx_comissao','idx_percentual','overhead','percentual_garantia','premio_seguro'])
        precificacao_data = {'codigo':pre_edit.codigo,'contratante': contratante,'qnt':0,'freq':0,'vigencia':vigencia,'marcem_precentual':0,'vlr_total':0,'criterio_jugamento':criterio_julgamento,'data_sessao':dt_sessao,'modo_disputa':modo_disputa,'objetp':objeto,'uf':uf,'idx_ctc_dolar_airtime':idx_ctc_dolar_airtime,'idx_ctc_dolar_antena':idx_ctc_dolar_antena,'idx_custos_financeiros':idx_custos_financeiros,'idx_oveheade':idx_oveheade,'idx_tx_importacao':idx_tx_importacao,'idx_comissao':idx_comissao,'idx_percentual':idx_percentual,'overhead':overhead,'percentual_garantia':percentual_garantia,'premio_seguro':premio_seguro}
        df_precificacao = pd.DataFrame(precificacao_data,index=[0])
        st.session_state.df_precificacao = pd.concat([st.session_state.df_precificacao, df_precificacao],ignore_index=True)
        
        if 'df_ma' not in st.session_state:
            st.session_state.df_ma = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ma_data = {'codigo':cod_item_ma,'cod_item': item_ma, 'vlr_venda':valor_ma,'qnt': quantidade_ma, 'percentual_desconto': percentual_ma, 'importacao': importacao_ma, 'franquia':franquia_ma,'cod_param_item':cod_param_item_ma}
        df_ma = pd.DataFrame(param_ma_data,index=[0])
        st.session_state.df_ma = pd.concat([st.session_state.df_ma, df_ma],ignore_index=True)

        if 'df_ml' not in st.session_state:
                st.session_state.df_ml = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_data = {'codigo':cod_item_ml,'cod_item': item_ml, 'vlr_venda':valor_ml,'qnt': quantidade_ml, 'percentual_desconto': percentual_ml, 'importacao': importacao_ml,'cod_param_item':cod_param_item_ml}
        df_ml = pd.DataFrame(param_ml_data,index=[0])
        st.session_state.df_ml = pd.concat([st.session_state.df_ml, df_ml],ignore_index=True)
        
        if 'df_mn' not in st.session_state:
            st.session_state.df_mn = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_mn_data = {'codigo':cod_item_mn,'cod_item': item_mn, 'vlr_venda':valor_mn,'qnt': quantidade_mn, 'percentual_desconto': percentual_mn, 'importacao': importacao_mn,'cod_param_item':cod_param_item_mn}
        df_mn = pd.DataFrame(param_mn_data,index=[0])
        st.session_state.df_mn = pd.concat([st.session_state.df_mn, df_mn],ignore_index=True)


        if 'df_mo' not in st.session_state:
            st.session_state.df_mo = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_mo_data = {'codigo':cod_item_mo,'cod_item': item_mo, 'vlr_venda':valor_mo,'qnt': quantidade_mo, 'percentual_desconto': percentual_mo, 'importacao': importacao_mo,'cod_param_item':cod_param_item_ml_mo}
        df_mo = pd.DataFrame(param_mo_data,index=[0])
        st.session_state.df_mo = pd.concat([st.session_state.df_mo, df_mo],ignore_index=True)

        if 'df_ml_eth' not in st.session_state:
                st.session_state.df_ml_eth = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_eth_data = {'codigo':cod_item_eth,'cod_item': item_ml_eth, 'vlr_venda':valor_ml_eth,'qnt': quantidade_ml_eth, 'percentual_desconto': percentual_ml_eth, 'importacao': importacao_ml,'cod_param_item':cod_param_item_ml}
        df_ml_eth = pd.DataFrame(param_ml_eth_data,index=[0])
        st.session_state.df_ml_eth = pd.concat([st.session_state.df_ml_eth, df_ml_eth],ignore_index=True)

        if 'df_ml_inv' not in st.session_state:
                st.session_state.df_ml_inv = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_inv_data = {'codigo':cod_item_inv,'cod_item': item_ml_inv, 'vlr_venda':valor_ml_inv,'qnt': quantidade_ml_inv, 'percentual_desconto': percentual_ml_inv, 'importacao': 0,'cod_param_item':cod_param_item_ml_inv}
        df_ml_inv = pd.DataFrame(param_ml_inv_data,index=[0])
        st.session_state.df_ml_inv = pd.concat([st.session_state.df_ml_inv, df_ml_inv],ignore_index=True)

        if 'df_ml_ptch' not in st.session_state:
                st.session_state.df_ml_ptch = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_ptch_data = {'codigo':cod_item_ptch,'cod_item': item_ml_ptch, 'vlr_venda':valor_ml_ptch,'qnt': quantidade_ml_ptch, 'percentual_desconto': percentual_ml_ptch, 'importacao': 0,'cod_param_item':cod_param_item_ml_ptch}
        df_ml_ptch = pd.DataFrame(param_ml_ptch_data,index=[0])
        st.session_state.df_ml_ptch = pd.concat([st.session_state.df_ml_ptch, df_ml_ptch],ignore_index=True)

        if 'df_ml_mala' not in st.session_state:
                st.session_state.df_ml_mala = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_mala_data = {'codigo':cod_item_mala,'cod_item': item_ml_mala, 'vlr_venda':valor_ml_mala,'qnt': quantidade_ml_mala, 'percentual_desconto': percentual_ml_mala, 'importacao': 0,'cod_param_item':cod_param_item_ml_mala}
        df_ml_mala = pd.DataFrame(param_ml_mala_data,index=[0])
        st.session_state.df_ml_mala = pd.concat([st.session_state.df_ml_mala, df_ml_mala],ignore_index=True)

        if 'df_ml_pio' not in st.session_state:
                st.session_state.df_ml_pio = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_pio_data = {'codigo':cod_item_pio,'cod_item': item_ml_pio, 'vlr_venda':valor_ml_pio,'qnt': quantidade_ml_pio, 'percentual_desconto': percentual_ml_pio, 'importacao': 0,'cod_param_item':cod_param_item_ml_pio}
        df_ml_pio = pd.DataFrame(param_ml_pio_data,index=[0])
        st.session_state.df_ml_pio = pd.concat([st.session_state.df_ml_pio, df_ml_pio],ignore_index=True)

        if 'df_ml_mon' not in st.session_state:
                st.session_state.df_ml_mon = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
        param_ml_mon_data = {'codigo':cod_item_mon,'cod_item': item_ml_mon, 'vlr_venda':valor_ml_mon,'qnt': quantidade_ml_mon, 'percentual_desconto': percentual_ml_mon, 'importacao': 0,'cod_param_item':cod_param_item_ml_mon}
        df_ml_mon = pd.DataFrame(param_ml_mon_data,index=[0])
        st.session_state.df_ml_mon = pd.concat([st.session_state.df_ml_mon, df_ml_mon],ignore_index=True)

        controle.editaPrecificacaoDataFile(df_precificacao,'data/precificacao.csv')
        controle.editaItensPrecificacaoDataFile(df_ma, df_ml,df_mn,df_mo,df_ml_eth,df_ml_inv,df_ml_mala,df_ml_mon,df_ml_pio,df_ml_ptch,'data/param_itens.csv',df_precificacao.codigo)
        
        st.success("Precificação editada com sucesso!")

else: st.warning("Selecine uma Precificação!")