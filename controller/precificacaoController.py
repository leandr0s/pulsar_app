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
    df = bf.read_gbq_query('select * from electric-armor-429218-g7.prf_cs.precificacao t1 \
                                inner join `electric-armor-429218-g7.prf_cs.log_precificacao`t2 on t1.codigo = t2.cod_precificacao \
                           where 1=1 \
                           or t2.status = "A" order by codigo \
                           limit '+str(limit))
    
    print(df)
    return df

def getDadosPrecificacao():
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
                           limit 3')
    return df