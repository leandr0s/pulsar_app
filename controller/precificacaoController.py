from datetime import datetime
import pandas as pd


# Caminho para o arquivo JSON da conta de serviço
SERVICE_ACCOUNT_FILE = "./config_param/electric-armor-429218-g7-f95603f613a1.json"
BUCKET_SILVER = "pulsar-transiente-zone"
BUCKET_GOLD = "pulsar-transiente-trust"
PROJECT_NAME = 'electric-armor-429218-g7'


def getPrecificacao(status,limit):
    df = pd.read_csv('data/precificacao.csv', sep=';')
    print(df)
    df2 = pd.read_csv('data/log_precificacao.csv', sep=';')
    df_final = pd.merge(df,df2, how='left', left_on='codigo', right_on='cod_precificacao')
    print(df_final)
    return df_final

def getDadosPrecificacao():
    df = pd.read_csv('data/precificacao.csv', sep=';')
    return df

def getDadosPrecificacaoSilverByCodigo(cod_precificacao):
    df = pd.read_csv('data/precificacao.csv', sep=';')
    return df

def getDadosPrecificacaoGoldByCodigo(cod_precificacao):
    df = pd.read_csv('data/precificacao.csv', sep=';')
    return df


