#%%

import os
from google.cloud import bigquery
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

sns.set_style()

%matplotlib inline

#%%

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../../data/credentials_bigquery.json"

client = bigquery.Client()
#%%

query_job = client.query("""
SELECT
     CAST(CONCAT(EXTRACT(YEAR FROM dtChamada), '-', EXTRACT(MONTH FROM dtChamada), '-1') AS DATE) AS mesAno
    ,COUNT(1) AS qtdChamada

FROM `project-tcc-434118.SILVER_ATD_CSR.tb_interacao_receptivo`


GROUP BY
    CAST(CONCAT(EXTRACT(YEAR FROM dtChamada), '-', EXTRACT(MONTH FROM dtChamada), '-1') AS DATE)        
""")

df = query_job.to_dataframe()

#%%

df['qtdChamadaLog'] = np.log10(df['qtdChamada'])
df['mesAno'] = pd.to_datetime(df['mesAno'], format="%m-%d-%Y")
df.info()

df.sort_values(by=['mesAno'], ascending=True, inplace=True)
df = df.reset_index()
df
#%%

df2 = df[df['qtdChamadaLog'] > 3.6]

list_mes = [x for x in range(1, len(df2) + 1)]  # Garantir que o comprimento corresponde a df2['qtdChamadaLog']
list_value = df2['qtdChamadaLog'].tolist()  # Converta diretamente para lista

fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(10, 10))

ax[0].hist(df2['qtdChamadaLog'], bins=30)
ax[1].scatter(list_mes, list_value)
ax[2].plot(df2['mesAno'], df2['qtdChamadaLog'])

plt.show()

# %%

# Correção do Seasonal Decompose e Plots
result = seasonal_decompose(df2['qtdChamadaLog'], model='additive', period=12)

# Plotar em tamanho maior
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(15, 8))
result.observed.plot(ax=ax1)
result.trend.plot(ax=ax2)
result.seasonal.plot(ax=ax3)
result.resid.plot(ax=ax4)

# Ajustar layout
plt.tight_layout()
plt.show()


# %%

#Aplicando MA

from statsmodels.tsa.arima_model import ARIMA
model = ARIMA(df2['qtdChamadaLog'], order=(0,0,1))
result_AR = model.fit(disp = -1)

print(result_AR)

# %%
