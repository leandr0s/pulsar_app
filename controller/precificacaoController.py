from datetime import datetime
import bigframes.pandas as bf
import pandas as pd
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
    df = pd.read_csv('..\\app\\data\\precificacao.csv', sep=';')
    print(df)
    df2 = pd.read_csv('..\\app\\data\\log_precificacao.csv', sep=';')
    df_final = pd.merge(df,df2, how='left', left_on='codigo', right_on='cod_precificacao')
    print(df_final)
    return df_final

def getDadosPrecificacao():
    df = pd.read_csv('..\\app\\data\\precificacao.csv', sep=';')
    return df

def getDadosPrecificacaoSilverByCodigo(cod_precificacao):
    df = pd.read_csv('..\\app\\data\\precificacao.csv', sep=';')
    return df

def getDadosPrecificacaoGoldByCodigo(cod_precificacao):
    df = pd.read_csv('..\\app\\data\\precificacao.csv', sep=';')
    return df


