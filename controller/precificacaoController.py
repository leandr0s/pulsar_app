from datetime import datetime
import pandas as pd
import numpy as np


# Caminho para o arquivo JSON da conta de serviço
SERVICE_ACCOUNT_FILE = "./config_param/electric-armor-429218-g7-f95603f613a1.json"
BUCKET_SILVER = "pulsar-transiente-zone"
BUCKET_GOLD = "pulsar-transiente-trust"
PROJECT_NAME = 'electric-armor-429218-g7'


def getPrecificacao(status,limit):
    df = pd.read_csv('data/precificacao.csv', sep=';')
    df2 = pd.read_csv('data/log_precificacao.csv', sep=';')
    df_final = pd.merge(df,df2, how='left', left_on='codigo', right_on='cod_precificacao')
    df_final = df_final[df_final.status == status]
    df_final = df_final.groupby(['contratante','uf','status']).agg(Maximum_Date=('dt_ultima_atualizacao', np.max)).reset_index()
    return df_final
def getFraquiaParamItem(cod_item,cod_param_item):
    df = pd.read_csv('data/param_itens.csv', sep=';')
    df = df[(df.cod_item == cod_item) & (df.codigo == cod_param_item)]
    franquia = 0
    if not df.empty:
        franquia = df.iloc[0]['franquia']
    return int(franquia)


def getMaxIdPrecificacao():
    df_log_anteriores = pd.read_csv('data/log_precificacao.csv', sep=';')

    df_ordenado = df_log_anteriores.sort_values(by=['cod_precificacao','dt_ultima_atualizacao','acao','status'], ascending=[True, True, True, True])
    max_id = int(df_ordenado.iloc[-1]['cod_precificacao'])
    return max_id
    


def getDadosPrecificacao(status,contratante):
    df = pd.read_csv('data/precificacao.csv', sep=';')
    df = df[df.contratante == contratante]
    df2 = pd.read_csv('data/log_precificacao.csv', sep=';')
    df_final = pd.merge(df,df2, how='left', left_on='codigo', right_on='cod_precificacao')

    df_final.drop(columns='qnt',axis=0, inplace=True)

    df4 = pd.read_csv('data/param_itens.csv', sep=';')
    df22 = pd.read_csv('data/grp_itens_prf.csv', sep=';')
    df33 = pd.read_csv('data/dados_itens.csv', sep=',')

    df4.rename(columns={'codigo' : 'cod_pram_iten'}, inplace=True)
    df33.rename(columns={'codigo' : 'cod_item'}, inplace=True)
    
    df_item_final = pd.merge(df4,df22, how='left', left_on='cod_pram_iten', right_on='cod_param_item')
    df_item_final = pd.merge(df_item_final,df33, how='left', left_on='cod_item', right_on='cod_item')
    df_item_final.to_csv('data/teste.csv', sep=';', index=False)
    df_final = pd.merge(df_final,df_item_final, how='left', left_on='cod_precificacao', right_on='cod_precificacao')

    df_final = df_final[df_final.status == status]
    
    return df_final

def getItemPrecificacao(cod_precificacao, status):
    df = pd.read_csv('data/param_itens.csv', sep=';')
    df2 = pd.read_csv('data/grp_itens_prf.csv', sep=';')
    df3 = pd.read_csv('data/dados_itens.csv', sep=',')
    
    df_final = pd.merge(df,df2, how='left', left_on='codigo', right_on='cod_param_item')
    df_final = pd.merge(df_final,df3, how='left', left_on='cod_item', right_on='codigo')
    df_edit = df_final[df_final.cod_precificacao == cod_precificacao]
    return df_edit


def getDadosPrecificacaoSilverByCodigo(cod_precificacao):
    df = pd.read_csv('data/precificacao.csv', sep=';')
    return df

def getDadosPrecificacaoGoldByCodigo(cod_precificacao):
    df = pd.read_csv('data/precificacao.csv', sep=';')
    return df


