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
