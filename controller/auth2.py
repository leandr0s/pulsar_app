import bigframes.pandas as bf
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.cloud import storage

# Caminho para o arquivo JSON da conta de serviço
SERVICE_ACCOUNT_FILE = "./config_param/electric-armor-429218-g7-f95603f613a1.json"

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

'''
blob = open(SERVICE_ACCOUNT_FILE)
key_content = str(blob.read())

try:
  os.mkdir("/metadata")
except Exception:
  print('o diretorio ja existe!')
# create a empty text file
fp = open(SERVICE_ACCOUNT_FILE, 'w')
fp.write(key_content)
fp.close()
'''
#credencial = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=BIG_QUERY_SCOPES)

def get_data_table(project,query_or_table,location,data):
    #atualiza tabela de precificacao    
    bf.options.bigquery.location = location
    bf.options.bigquery.project = project    
    bucket_repository = "pulsar-transiente-zone"
    
    bf_table = bf.read_gbq(query_or_table)
    df = bf_table.to_pandas()
    #df.to_gbq(destination_table=query_or_table, project_id=project , if_exists='append', credentials=credentialsBigQuery)
    print(df)
    upload_blob(df)
    #storage_client = storage.Client()
    #bucket = storage_client.bucket(bucket_repository)
    #bucket.blob('teste.csv').upload_from_string(df.to_csv(header=True,sep=';',index=False), 'text/csv')
    

# Exemplo: Acessar a API do Google Cloud Storage
def list_gcs_buckets(project_id):
    # Cria o cliente para a API Cloud Storage
    service = build("storage", "v1", credentials=credentials)

    # Lista os buckets no projeto
    request = service.buckets().list(project=project_id)
    response = request.execute()

    # Exibe os buckets encontrados
    if "items" in response:
        for bucket in response["items"]:
            print(f"Bucket: {bucket['name']}")
    else:
        print("Nenhum bucket encontrado.")

    bucket_transient = response["items"][1]
    print('recuperando bucket')
    print(bucket_transient)
    storage_client = storage.Client()


def upload_blob(df):
    bucket_name = "pulsar-transiente-zone"

    storage_client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_FILE)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob("teste.csv")
    blob.upload_from_string(df.to_csv(header=True,sep=';',index=False), 'text/csv')
    
    '''
    blob.write(df.to_csv(header=True,sep=';',index=False))
    blob.close()
    generation_match_precondition = 1
    blob.upload_from_filename("teste.csv", if_generation_match=generation_match_precondition)

    '''

if __name__ == "__main__":
    # Substitua pelo ID do seu projeto
    LOCATION = "us-east4"
    PROJECT_ID = "electric-armor-429218-g7"
    QUERY_OR_TABLE = "electric-armor-429218-g7.prf_cs.log_precificacao"
    list_gcs_buckets(PROJECT_ID)
    get_data_table(PROJECT_ID,QUERY_OR_TABLE,LOCATION,[])


