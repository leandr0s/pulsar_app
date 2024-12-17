# %%
# With BigQuery DataFrames, you can use many familiar Pandas methods, but the
# processing happens BigQuery rather than the runtime, allowing you to work with larger
# DataFrames that would otherwise not fit in the runtime memory.
# Learn more here: https://cloud.google.com/python/docs/reference/bigframes/latest
import pandas as pd
import bigframes.pandas as bf
# Imports the Google Cloud client library
from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account
import os
#from google.auth import impersonated_credentials
#from google.oauth2.credentials import Credentials
#from googleapiclient.discovery import build

#electric-armor-429218-g7.prf_cs.grp_cstos_grp_rec_imp

bf.options.bigquery.location = "us-east4" #this variable is set based on the dataset you chose to query
bf.options.bigquery.project = "electric-armor-429218-g7" #this variable is set based on the dataset you chose to query
# The name for the new bucket
bucket_name = "pulsar-transiente-trust"
bucket_repository = "pulsar-transiente-zone"
blob_name = './config_param/electric-armor-429218-g7-f95603f613a1.json'
credencial = ''
path_credencial = '/metadata/token.json'
key_content = ''
scopes = ['https://www.googleapis.com/auth/bigquery']

# %%
from google.cloud import storage

os.environ.setdefault("GCLOUD_PROJECT", "electric-armor-429218-g7")

#storage_client = storage.Client()
#bucket = storage_client.bucket(bucket_repository)
blob = open(blob_name)
key_content = str(blob.read())
print(key_content)
'''
with blob.open("r") as f:
        key_content = f.read()
        print('teste###############')
        print(key_content)
'''
        
# %%
try:
  os.mkdir("/metadata")
except Exception:
  print('o diretorio ja existe!')
# create a empty text file
fp = open(path_credencial, 'w')
fp.write(key_content)
fp.close()

# %%
credencial = service_account.Credentials.from_service_account_file(path_credencial,scopes=scopes)

# %%
#atualiza camada rom com os novos dados, cadastro do app



#atualiza tabela de precificacao
bf_precificacao = bf.read_csv('gs://pulsar-transiente-zone/precificacao/precificacao.csv', sep=';')
df_precificacao = bf_precificacao.to_pandas()

print(df_precificacao)

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