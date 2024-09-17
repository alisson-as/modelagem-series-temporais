#%%
import json
import requests
from datetime import date
from datetime import timedelta
from google.cloud import bigquery
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.types import StructType, StructField, StringType

#%%

# Definindo variável de ambiente para a chave de conta de serviço GCP
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../../data/credentials_bigquery.json"

# Inicializar o cliente GCP
client = bigquery.Client()

# Definindo ID projeto GCP e tabela para carregamento dos dados
project_id = 'project-tcc-434118'
dataset_id = 'BRONZE_ATD_CSR'
table_id = 'tb_interactions'
table_ref = client.dataset(dataset_id, project=project_id).table(table_id)

# Inicializar a sessão do Spark
# Inicialize o SparkSession
spark = SparkSession.builder.getOrCreate()

#%%

# Definindo data d-7 para coletar dados sempre considerando 7 dias antes da data de consulta
dt_today = date.today()
dt_ref = '2023-01-01'# date.today() - timedelta(days=7)

#%%

def get_data_api(dt_ref):
    # Coletando informações para conexão
    with open("../../data/api_config.json", "r") as j_file:
        config_api = json.load(j_file)

    # Criando a string de filtro
    filter_dataset = f"callstartdt>='{dt_ref}'"

    # Construindo a URL da requisição
    url = f"https://{config_api['url']}/resource/{config_api['dataset']}.json"

    # Definindo os parâmetros da consulta
    params = {
        "$where": filter_dataset,
        #"$limit": 20,
        "$$app_token": config_api["app_token"]
    }

    # Autenticação (caso necessário)
    auth = (config_api["username"], config_api["password"])

    # Fazendo a requisição GET
    response = requests.get(url, params=params, auth=auth)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Convertendo o resultado em JSON
        results = response.json()
        
        # Convertendo para DataFrame
        df = spark.createDataFrame(results)
        
        df = df.withColumn('DT_PROCESSAMENTO', lit(dt_today))
        # Retornando DataFrame
        
        for old, new in {item: item.upper() for item in df.columns}.items():
            df = df.withColumnRenamed(old, new) 
        
        return df
    else:
        return print(f"Erro na requisição: {response.status_code} \n {response.text}")

df_final = get_data_api(dt_ref)

#%%

# Coletando lista de IDs na tabela no BigQuery
existing_ids = [row.UNIQUE_ID for row in client.query(
    f"""SELECT 
            UNIQUE_ID 
        FROM {project_id}.{dataset_id}.{table_id}
    """
).result()]

#%%
existing_ids_tuples = [(id,) for id in existing_ids]

schema = StructType([
    StructField("UNIQUE_ID", StringType(), nullable=True)
])

df_existing_ids = spark.createDataFrame(existing_ids_tuples, schema=schema)
df_existing_ids.show()

df_final_filter = df_final.join(df_existing_ids, on="UNIQUE_ID", how="left_anti")

#%%
df_final_filter_pd = df_final_filter.toPandas()

# Inserir os dados no BigQuery
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, 
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND
)

job = client.load_table_from_dataframe(df_final_filter_pd, table_ref, job_config=job_config) 
job.result()  # Aguarde a conclusão do trabalho

print(f"Inseridos {job.output_rows} linhas na tabela {table_id}")
