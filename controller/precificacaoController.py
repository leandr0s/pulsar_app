from datetime import datetime
import bigframes.pandas as bf
import pandas as pd
import pydata_google_auth
import google.cloud.bigquery
from controller import auth2 as au
from google.cloud import storage
from google.oauth2 import service_account
from googleapiclient.discovery import build


# Caminho para o arquivo JSON da conta de serviço
SERVICE_ACCOUNT_FILE = "./config_param/electric-armor-429218-g7-f95603f613a1.json"
BUCKET_SILVER = "pulsar-transiente-zone"
BUCKET_GOLD = "pulsar-transiente-trust"
PROJECT_NAME = 'electric-armor-429218-g7'

#this variable is set based on the dataset you chose to query
bf.options.bigquery.location = "us-east4" 
#this variable is set based on the dataset you chose to query
bf.options.bigquery.project = "electric-armor-429218-g7" 



def getPrecificacao(status,limit):

    credentialBQ = au.getCredentialBigQuery(SERVICE_ACCOUNT_FILE)
    credential = au.getCredentialFromJson(SERVICE_ACCOUNT_FILE)
    df = bf.read_gbq_query('select distinct codigo as cod_precificacao, contratante, vigencia, uf,idx_custos_financeiros, acao, status \
                            from electric-armor-429218-g7.prf_cs.precificacao t1 \
                                inner join `electric-armor-429218-g7.prf_cs.log_precificacao`t2 on t1.codigo = t2.cod_precificacao \
                           where 1=1 \
                           and t2.status = "'+status+'" order by codigo \
                           limit '+str(limit))
    
    #print(df)
    return df

def getDadosPrecificacao():
    df = bf.read_gbq_query('select distinct t1.cod_precificacao \
                                ,contratante \
                                ,vlr_total \
                                ,vigencia \
                                ,desc_item \
                                ,custo_ref \
                                ,categoria \
                                ,qnt \
                                ,valor_ponto \
                                ,preco_total \
                                ,peso_item_proj \
                                ,und \
                                ,cod_grupo \
                                ,faturamento \
                                ,cotacao_dolar_airtime \
                                ,cotacao_dolar_antena \
                                ,custos_financeiros \
                                ,ovehead \
                                ,tx_importacao \
                                ,comissao \
                                ,percentual \
                                ,grp_categoria \
                                ,percentual_garantia \
                                ,premio_seguro \
                                ,cod_param_item \
                                ,importacao \
                                ,overhead \
                                ,cod_item \
                                ,t2.acao \
                                ,t2.status \
                                ,t2.dt_criacao \
                                ,t2.dt_ultima_atualizacao \
                                FROM `electric-armor-429218-g7.prf_cs.vw_silver_dados_precificacao` t1 \
                                inner join `electric-armor-429218-g7.prf_cs.log_precificacao`t2 on t1.cod_precificacao = t2.cod_precificacao \
                           limit 3')
    return df

def getDadosPrecificacaoSilverByCodigo(cod_precificacao):
    df = bf.read_gbq_query('SELECT distinct t1.cod_precificacao \
                                ,contratante \
                                ,vlr_total \
                                ,vigencia \
                                ,desc_item \
                                ,custo_ref \
                                ,categoria \
                                ,qnt \
                                ,valor_ponto \
                                ,preco_total \
                                ,peso_item_proj \
                                ,und \
                                ,cod_grupo \
                                ,faturamento \
                                ,cotacao_dolar_airtime \
                                ,cotacao_dolar_antena \
                                ,custos_financeiros \
                                ,ovehead \
                                ,tx_importacao \
                                ,comissao \
                                ,percentual \
                                ,grp_categoria \
                                ,percentual_garantia \
                                ,premio_seguro \
                                ,cod_param_item \
                                ,importacao \
                                ,overhead \
                                ,cod_item \
                                ,t2.acao \
                                ,t2.status \
                                ,t2.dt_criacao \
                                ,t2.dt_ultima_atualizacao \
                                FROM `electric-armor-429218-g7.prf_cs.vw_silver_dados_precificacao` t1 \
                                inner join `electric-armor-429218-g7.prf_cs.log_precificacao`t2 on t1.cod_precificacao = t2.cod_precificacao \
                                where t1.cod_precificacao = '+ str(cod_precificacao) \
                           +' limit 3')
    return df

def getDadosPrecificacaoGoldByCodigo(cod_precificacao):
    df = bf.read_gbq_query('SELECT distinct t1.cod_precificacao \
                                ,contratante \
                                ,vlr_total \
                                ,vigencia \
                                ,desc_item \
                                ,custo_ref \
                                ,categoria \
                                ,qnt \
                                ,valor_ponto \
                                ,preco_total \
                                ,peso_item_proj \
                                ,und \
                                ,cod_grupo \
                                ,faturamento \
                                ,cotacao_dolar_airtime \
                                ,cotacao_dolar_antena \
                                ,custos_financeiros \
                                ,ovehead \
                                ,tx_importacao \
                                ,comissao \
                                ,percentual \
                                ,grp_categoria \
                                ,percentual_garantia \
                                ,premio_seguro \
                                ,cod_param_item \
                                ,importacao \
                                ,overhead \
                                ,cod_item \
                                FROM `electric-armor-429218-g7.prf_cs.gold_dados_precificacao` t1 \
                                where t1.cod_precificacao = '+ str(cod_precificacao))
    return df

def getCustosHardwareSilver(cod_precificacao,tipo_custo):
    df = bf.read_gbq_query('select cod_precificacao, custos, vlr_custos \
                           from electric-armor-429218-g7.prf_cs.vw_silver_custos where 1=1 \
                           and custos = "Hardware" and cod_precificacao = '+str(cod_precificacao) )
    print(df)
    return df['vlr_custos'].iloc[0]

def getCustosGoldPrecificacao(cod_precificacao):
    df = bf.read_gbq_query('select cod_precificacao, custos, vlr_custos \
                           from electric-armor-429218-g7.prf_cs.gold_custos where 1=1 \
                           and cod_precificacao = '+str(cod_precificacao) )
    return df

def getImpostosGoldPrecificacao(cod_precificacao):
    df = bf.read_gbq_query('select cod_precificacao, imposto, vlr_impostos \
                           from electric-armor-429218-g7.prf_cs.gold_impostos where 1=1 \
                           and cod_precificacao = '+str(cod_precificacao) )
    return df

def getCustosHardwareSilver(cod_precificacao,tipo_custo):
    df = bf.read_gbq_query('select cod_precificacao, custos, vlr_custos \
                           from electric-armor-429218-g7.prf_cs.vw_silver_custos where 1=1 \
                           and custos = "Hardware" and cod_precificacao = '+str(cod_precificacao) )
    print(df)
    return df['vlr_custos'].iloc[0]

def getCustosSilverPrecificacao(cod_precificacao):
    df = bf.read_gbq_query('select cod_precificacao, custos, vlr_custos \
                           from electric-armor-429218-g7.prf_cs.vw_silver_custos where 1=1 \
                           and cod_precificacao = '+str(cod_precificacao) )
    return df

def getImpostosSilverPrecificacao(cod_precificacao):
    df = bf.read_gbq_query('select cod_precificacao, imposto, vlr_impostos \
                           from electric-armor-429218-g7.prf_cs.vw_silver_impostos where 1=1 \
                           and cod_precificacao = '+str(cod_precificacao) )
    return df

def getTpCstoFinanceiro():
    df = bf.read_gbq_query('select distinct custos from electric-armor-429218-g7.prf_cs.vw_silver_custos')
    return df

