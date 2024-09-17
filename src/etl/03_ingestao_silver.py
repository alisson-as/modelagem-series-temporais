#%%
from google.cloud import bigquery
import os

#%%
# Definindo variável de ambiente para a chave de conta de serviço GCP
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../../data/credentials_bigquery.json"

# Inicializar o cliente GCP
client = bigquery.Client()

#%%

with open('ingestao_silver.sql', 'r') as file_query:
    query_criacao = file_query.read()

execute_job = client.query(query_criacao)

execute_job.result()

print(f"Criação concluído na tabela project-tcc-434118.SILVER_ATD_CSR.tb_interacao_receptivo")