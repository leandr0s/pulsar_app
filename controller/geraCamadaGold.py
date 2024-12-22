import bigframes.pandas as bf
import os
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


def getServiceAccountFile():
    return SERVICE_ACCOUNT_FILE

def gravaDadosNaCamadaSilver(df,storage_client,file_name):
    '''
    os.environ.setdefault("GCLOUD_PROJECT", "electric-armor-429218-g7")
    # Escopos que a aplicação precisa acessar
    SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
    BIG_QUERY_SCOPES = ["https://www.googleapis.com/auth/bigquery"]

    # Autenticar usando a conta de serviço
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    # Autenticar usando a conta de serviço
    credentialsBigQuery = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=BIG_QUERY_SCOPES
    )
    
    service = build("storage", "v1", credentials=credentials)
    '''
    #storage_client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_FILE)
    bucket = storage_client.bucket(BUCKET_SILVER)
    blob = bucket.blob(file_name)
    print(df)
    blob.upload_from_string(df.to_csv(header=True,sep=';',index=False), 'text/csv')
    print("Dados gravado com sucesso!")

def gravaDadosNaCamadaGold(table_name):
    df_silver = bf.read_gbq(table_name)
    df_gold = df_silver.to_pandas()
    df_gold.to_gbq(destination_table=PROJECT_NAME+'.'+table_name, project_id=PROJECT_NAME , if_exists='replace', credentials=credencial)
    print("Dados gravado com sucesso!")

'''

#atualiza tabela de precificacao
bf_precificacao = bf.read_csv('gs://pulsar-transiente-zone/precificacao/precificacao.csv', sep=';')
df_precificacao = bf_precificacao.to_pandas()

print(df_precificacao)

'''
'''
df_precificacao.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.precificacao', project_id='electric-armor-429218-g7' , if_exists='append', credentials=credencial)

#atualiza tabela de param itens
bf_param_itens = bf.read_csv('gs://pulsar-transiente-zone/param_itens/param_itens.csv', sep=';')
df_param_itens = bf_param_itens.to_pandas()
df_param_itens.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.param_itens', project_id='electric-armor-429218-g7' , if_exists='append', credentials=credencial)

#atualiza tabela de grupo itens da precificacao
bf_grp_itens_prf = bf.read_csv('gs://pulsar-transiente-zone/grp_itens_prf/grp_itens_prf.csv', sep=';' )
df_grp_itens_prf = bf_grp_itens_prf.to_pandas()
df_grp_itens_prf.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.grp_itens_prf', project_id='electric-armor-429218-g7' , if_exists='append', credentials=credencial)

#atualiza tabela de log precificacao
bf_log_precificacao = bf.read_csv('gs://pulsar-transiente-zone/log_precificacao/log_precificacao.csv', sep=';' )
df_log_precificacao = bf_log_precificacao.to_pandas()
df_log_precificacao.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.log_precificacao', project_id='electric-armor-429218-g7' , if_exists='append', credentials=credencial)


# %%
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)

# %%
#recupera os dados da precificação
df_silver_dados_prf = bf.read_gbq("prf_cs.vw_silver_dados_precificacao")
bucket.blob('gold_dados_precificacao.csv').upload_from_string(df_silver_dados_prf.to_csv(header=True,sep=';',index=False), 'text/csv')


# %% [markdown]
# 

# %%
df_gold_dados_prf = df_silver_dados_prf.to_pandas()
df_gold_dados_prf.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.gold_dados_precificacao', project_id='electric-armor-429218-g7' , if_exists='replace', credentials=credencial)

# %%
#recupera os dados de custos
df_silver_custos = bf.read_gbq("prf_cs.vw_silver_custos")
bucket.blob('gold_custos.csv').upload_from_string(df_silver_custos.to_csv(header=True,sep=';',index=False), 'text/csv')
#df_silver_custos.head(3)




# %%
df_gold_custos = df_silver_custos.to_pandas()
df_gold_custos.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.gold_custos', project_id='electric-armor-429218-g7' , if_exists='replace', credentials=credencial)

# %%
#recupera os dados de impostos da precificação
df_silver_impostos = bf.read_gbq("prf_cs.vw_silver_impostos")
bucket.blob('gold_impostos.csv').upload_from_string(df_silver_impostos.to_csv(header=True,sep=';',index=False), 'text/csv')
#df_silver_impostos.head(3)

# %%
df_gold_impostos = df_silver_impostos.to_pandas()
df_gold_impostos.to_gbq(destination_table='electric-armor-429218-g7.prf_cs.gold_impostos', project_id='electric-armor-429218-g7' , if_exists='replace', credentials=credencial)


'''