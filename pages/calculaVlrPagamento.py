import pandas as pd
import streamlit as st
import controller.geraCamadaGold as controle

from controller import precificacaoController as pr


st.title("Calcula o Valor de pagamento para a Precificação")

st.caption("Dados da precificação")

df_precificacao = pr.getPrecificacao('A',20)
#df_tp_csto_financeito = pr.getTpCstoFinanceiro()

col1, col2 = st.columns(2)
with col1:
    contratante = None
    contratante = st.selectbox('Selecione Precificação', df_precificacao.contratante)
    #csto_financeiro = st.selectbox('Selecione o Custo Financeiro', df_tp_csto_financeito.custos) 

    #print(df_precificacao[df_precificacao.contratante == contratante]['vigencia'].iloc[0])    
    

if st.button('Calcula'):
    if contratante != None:
        st.balloons()
        print(df_precificacao[df_precificacao.contratante == contratante])    
        cod_precificacao = df_precificacao[df_precificacao.contratante == contratante]['cod_precificacao'].iloc[0]
        tx_cto_financeiro = df_precificacao[df_precificacao.contratante == contratante]['idx_custos_financeiros'].iloc[0]
        vigencia = df_precificacao[df_precificacao.contratante == contratante]['vigencia'].iloc[0]
        csto_financeiro = 'Hardware'
        vlr_cto_hardware = 0
        vlr_parcela = 0
        st.code("Tx.Csto_Financeiro = "+str(tx_cto_financeiro))
        st.code("Csto_Hardware = "+str(vlr_cto_hardware))
        st.code("Vigencia = "+str(vigencia))
        st.code("Parcela = "+str(vlr_parcela))
        st.latex(r''' Parcela = (Tx.Csto_Financeiro * Csto_Hardware * Vigencia) \ Vigencia ''')
        st.info("Custo financeiro calculado com sucesso!")
    else: st.warning("É obrigatorio selecionar a Precificação e o Tipo do Custo!")