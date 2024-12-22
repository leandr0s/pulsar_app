import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.cloud import storage

os.environ.setdefault("GCLOUD_PROJECT", "electric-armor-429218-g7")

# Escopos que a aplicação precisa acessar
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
BIG_QUERY_SCOPES = ["https://www.googleapis.com/auth/bigquery"]

def getCredentialGCP(SERVICE_ACCOUNT_FILE):
    # Autenticar usando a conta de serviço
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return credentials

def getCredentialBigQuery(SERVICE_ACCOUNT_FILE):
    # Autenticar usando a conta de serviço
    credentialsBigQuery = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=BIG_QUERY_SCOPES
        )
    return credentialsBigQuery

def getCredentialFromJson(SERVICE_ACCOUNT_FILE):
    credential = storage.Client.from_service_account_json(SERVICE_ACCOUNT_FILE)
    return credential




