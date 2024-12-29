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


def __getClientBQ(SERVICE_ACCOUNT_FILE,PROJECT_NAME):
    credentials = pydata_google_auth.load_user_credentials(
        SERVICE_ACCOUNT_FILE,
    )
    client = google.cloud.bigquery.BigQueryClient(
        credentials=credentials,
        project=PROJECT_NAME
    )
    return client

def getServiceAccountFile():
    return SERVICE_ACCOUNT_FILE

def gravaPrecificacaoNaCamadaSilver(df,storage_client,file_name,big_query_credential):
    
    df['codigo'] = __getProximoId('electric-armor-429218-g7.prf_cs.precificacao')
    #print(Entidade.table_name[Entidade.PRECIFICACAO])
    bucket = storage_client.bucket(BUCKET_SILVER)
    blob = bucket.blob(file_name)
    blob.upload_from_string(df.to_csv(header=True,sep=';',index=False), 'text/csv')
    df['data_sessao'] = str(df['data_sessao'])
    df.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.precificacao', project_id=PROJECT_NAME , if_exists='append', credentials=big_query_credential)
    print("Precificacao gravado com sucesso!")

def gravaDadosNaCamadaGold(table_name,file_name,credencial,credentialBQ):
    df_silver = bf.read_gbq(table_name)
    storage_client = storage.Client()
    bucket = credencial.bucket(BUCKET_GOLD)
    print(df_silver)
    df_gold = df_silver.to_pandas()
    bucket.blob(file_name).upload_from_string(df_gold.to_csv(header=True,sep=';',index=False), 'text/csv')
    df_gold.to_gbq(destination_table=table_name, project_id=PROJECT_NAME , if_exists='replace', credentials=credentialBQ)
    print("Dados gravado com sucesso!")

def gravaItensPrecificacaoNaCamadaSilver(df_ma, df_ml,df_mn,df_mo,storage_client,file_name, big_query_credential):
    ultimo_cod_param_item = __getProximoId('electric-armor-429218-g7.prf_cs.param_itens')
    cod_precificacao = __getProximoId('electric-armor-429218-g7.prf_cs.precificacao')

    df = pd.DataFrame(columns=['codigo','cod_item','vlr_venda','qnt','percentual_desconto','importacao'])
    dados_grp_itens = []
    
    if df_ma['qnt'].iloc[0] > 0:
        cod_item = bf.read_gbq_query('select t1.codigo from electric-armor-429218-g7.prf_cs.itens t1 where t1.objeto = \''+ str(df_ma['cod_item'].iloc[0]) + '\'')
        df_ma['cod_item'].iloc[0] = cod_item.iloc[0]['codigo']
        df_ma['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'MA',cod_precificacao])
        ultimo_cod_param_item = ultimo_cod_param_item +1        
        df = pd.concat([df,df_ma],ignore_index=True)
        
        
    if df_ml['qnt'].iloc[0] > 0:
        cod_item = bf.read_gbq_query('select t1.codigo from electric-armor-429218-g7.prf_cs.itens t1 where t1.objeto = \''+ str(df_ml['cod_item'].iloc[0]) + '\'')
        df_ml['cod_item'].iloc[0] = cod_item.iloc[0]['codigo']
        df_ml['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'ML',cod_precificacao])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_ml],ignore_index=True)
        
    if df_mn['qnt'].iloc[0] > 0:
        df_mn['cod_item'].iloc[0] = 16
        df_mn['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'MN',cod_precificacao])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_mn],ignore_index=True)
        
    if df_mo['qnt'].iloc[0] > 0:
        df_mo['cod_item'].iloc[0] = 17
        df_mo['codigo'].iloc[0] = ultimo_cod_param_item
        dados_grp_itens.append([ultimo_cod_param_item,'MO',cod_precificacao])
        ultimo_cod_param_item = ultimo_cod_param_item +1
        df = pd.concat([df,df_mo],ignore_index=True)
    
    df_grp_itens = pd.DataFrame(dados_grp_itens,columns=['cod_param_item','cod_grupo','cod_precificacao'])
    
    __assossiaGrpItem(df_grp_itens,storage_client,big_query_credential)
    __geraLogPrecificacao(cod_precificacao,'I','A',storage_client,big_query_credential)
    
    bucket = storage_client.bucket(BUCKET_SILVER)
    blob = bucket.blob(file_name)
    blob.upload_from_string(df.to_csv(header=True,sep=';',index=False), 'text/csv')
    df.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.param_itens', project_id=PROJECT_NAME , if_exists='append', credentials=big_query_credential)
    print("Itens gravado com sucesso!")

def __assossiaGrpItem(df,storage_client,big_query_credential):
    bucket = storage_client.bucket(BUCKET_SILVER)
    blob = bucket.blob('grp_itens_prf/grp_itens_prf.csv')
    blob.upload_from_string(df.to_csv(header=True,sep=';',index=False), 'text/csv')
    df.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.grp_itens_prf', project_id=PROJECT_NAME , if_exists='append', credentials=big_query_credential)
    print("Grupo Itens gravado com sucesso!")

def __getProximoId(table_name):
    id = bf.read_gbq_query('select max(codigo) as codigo from '+table_name)
    return id.iloc[0]['codigo']+1

def __geraLogPrecificacao(cod_precificacao,acao,status,storage_client,big_query_credential):
    data_atual = datetime.today()
    dt_atual_str = data_atual.strftime('%d/%m/%y %H:%M')
    print(dt_atual_str)
    log_data = [[cod_precificacao,acao,status,dt_atual_str,dt_atual_str]]
    
    #storage_client = storage.Client()
    df_log = pd.DataFrame(data=log_data,columns=['cod_precificacao','acao','status','dt_ultima_atualizacao','dt_criacao'])
    bucket = storage_client.bucket(BUCKET_SILVER)
    blob = bucket.blob('log_precificacao/log_precificacao.csv')
    blob.upload_from_string(df_log.to_csv(header=True,sep=';',index=False), 'text/csv')
    df_log.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.log_precificacao', project_id=PROJECT_NAME , if_exists='append', credentials=big_query_credential)
    print("Log gravado com sucesso!")

def atualizaCamadaSilver(location,table,credencial):  
     
    #atualiza tabela de precificacao
    bfq = bf.read_csv(location, sep=';')
    df = bfq.to_pandas()
    df.to_gbq(destination_table=table, project_id=PROJECT_NAME , if_exists='append', credentials=credencial)
    print("Dados gravado com sucesso!") 

