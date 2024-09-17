#%%

from google.cloud import bigquery
import os
from datetime import date

#%%

dt_today = date.today()

# Definindo variável de ambiente para a chave de conta de serviço GCP
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../../data/credentials_bigquery.json"

# Inicializar o cliente GCP
client = bigquery.Client()

# Definindo ID projeto GCP e tabela para carregamento dos dados
dataset_id = 'project-tcc-434118.BRONZE_ATD_CSR'
table_id = 'tb_interactions'

#%% 
# Define o esquema da tabela que vai ser criada e carregado os dados
schema = [
    bigquery.SchemaField("AGENTDISPID", "STRING"),
    bigquery.SchemaField("CALLSTARTDT", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("CALLACTIONID", "STRING"),
    bigquery.SchemaField("CALLACTIONREASONID", "STRING"),
    bigquery.SchemaField("CALLID", "STRING"),
    bigquery.SchemaField("CALLTYPEID", "STRING"),
    bigquery.SchemaField("CONNCLEARDT", "STRING"),
    bigquery.SchemaField("DNIS", "STRING"),
    bigquery.SchemaField("QUEUEENDDT", "STRING"),
    bigquery.SchemaField("SEQNUM", "STRING"),
    bigquery.SchemaField("SERVICE_ID", "STRING"),
    bigquery.SchemaField("STATION", "STRING"),
    bigquery.SchemaField("WORKGROUP_ID", "STRING"),
    bigquery.SchemaField("WRAPENDDT", "STRING"),
    bigquery.SchemaField("QUEUESTARTDT", "STRING"),
    bigquery.SchemaField("PREVIEWENDDT", "STRING"),
    bigquery.SchemaField("PREVIEWSTARTDT", "STRING"),
    bigquery.SchemaField("ANSWERDT", "STRING"),
    bigquery.SchemaField("ANSWER_SPEED_SECS", "STRING"),
    bigquery.SchemaField("TALK_TIME_SECS", "STRING"),
    bigquery.SchemaField("WRAP_TIME_SECS", "STRING"),
    bigquery.SchemaField("SERVICE_LEVEL", "STRING"),
    bigquery.SchemaField("ABANDONED", "STRING"),
    bigquery.SchemaField("CALL_TYPE", "STRING"),
    bigquery.SchemaField("UNIQUE_ID", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("ANSWERED", "STRING"),
]

# Configurar job de carremento 
job_config = bigquery.LoadJobConfig(
    schema=schema,
    source_format=bigquery.SourceFormat.CSV, # Difinindo tipo do arquivo presente no bucket da Cloud Storage
)

# Caminho do arquivo presente no bucket
uri = "gs://base_registro_calls/dados_brutos/Citizen_Service_Request__CSR__Call_Center_Calls_20240830.csv"

# Carregamento para carregamento do Job para criação da tabela
load_job = client.load_table_from_uri(
    uri,
    f"{dataset_id}.{table_id}",
    job_config=job_config
)

# Comando para aguardar a criação do Job, fazendo com que não haja execução de outro código até a finalização
load_job.result()

def import_query(path):
    with open(path, "r") as file_query:
        query_aux = file_query.read()

    return query_aux

query_fmt = import_query("inserir_dt_processamento.sql").format(date=dt_today)

query_job = client.query(query_fmt)

query_job.result()

print(f"Carregamento concluído na tabela {table_id}")
#%%