# %%

from google.cloud import bigquery
import os

# %%

# Variável de ambiente para a chave de conta de serviço
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../../data/credentials_bigquery.json"

# Inicializar o cliente
client = bigquery.Client()

dataset_id = 'project-tcc-434118.BRONZE_ATD_CSR'
table_id = 'tb_interactions'

#%% 
# Define o esquema da tabela
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
    source_format=bigquery.SourceFormat.CSV,
)

uri = "gs://base_registro_calls/dados_brutos/Citizen_Service_Request__CSR__Call_Center_Calls_20240830.csv"

load_job = client.load_table_from_uri(
    uri,
    f"{dataset_id}.{table_id}",
    job_config=job_config
)

load_job.result()  # Job de carregamento

print(f"Carregamento concluído na tabela {table_id}")
# %%
