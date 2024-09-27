#%%
import pandas as pd
import os
import chardet
from pathlib import Path
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# %%

list_file = os.listdir("../../../base_projects/temperature_data")
file_path = Path(f"../../../base_projects/temperature_data/{list_file[0]}")
# Abrir o arquivo no modo binário para detecção de encoding
with open(file_path, 'rb') as f:
    encoding = f"'{chardet.detect(f.read())['encoding']}'"
print(encoding)

print(list_file.index('INMET_SE_SP_A771_SAO PAULO - INTERLAGOS_01-01-2023_A_31-12-2023.CSV'))
index_file = list_file.index('INMET_SE_SP_A771_SAO PAULO - INTERLAGOS_01-01-2023_A_31-12-2023.CSV')
#%%
df = pd.read_csv(
        f"../../../base_projects/temperature_data/{list_file[index_file]}",
        sep=";", 
        skiprows=8,
        encoding=encoding
    )
df = df[['Data', 'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)']]
df.rename(columns={'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)': 'Temperatura do Ar (°C)'}, inplace=True)
df
#%%
df.info()
# %%

df['Data'] = pd.to_datetime(df['Data'], format='%Y/%m/%d')
df['Temperatura do Ar (°C)'] = (df['Temperatura do Ar (°C)']
    .str
    .replace(',','.')
    .astype(float)
)
data_diario = df.groupby('Data')['Temperatura do Ar (°C)'].mean().reset_index()
data_diario.columns = ['Data', 'Temperatura Média Diária (°C)']

df_diario = pd.DataFrame(data_diario)
df_diario
# %%
df_diario.info()

# %%

fig, ax = plt.subplots(figsize=(15, 8))

ax.plot(
    df_diario['Data'], 
    df_diario['Temperatura Média Diária (°C)'], 
    linewidth=1.5,
    color='#4169E1'
)
# ax.set_title('Temperatura Média Diária (°C) - Mirante de Santana - São Paulo', fontsize=20)
ax.set_xlabel('Data', fontsize=14)
#ax.grid(True, linestyle='--', alpha=1, color='gray')
ax.set_facecolor(color='whitesmoke')
ax.tick_params(axis='both', which='major', labelsize=16)

#borda
ax.spines['top'].set_color('lightgray')       # Borda superior
ax.spines['right'].set_color('lightgray')     # Borda direita
ax.spines['bottom'].set_color('lightgray')    # Borda inferior
ax.spines['left'].set_color('lightgray')      # Borda esquerda

# ax.spines['top'].set_linewidth(1)         # Espessura da borda superior


plt.tight_layout()
plt.show()
# %%

def plot_ax(y, ax, title):
    
    ax.plot(
        df_diario['Data'], 
        y, 
        linewidth=1.5,
        color='#4169E1'
    )
    ax.set_title(title, fontsize=15)
    #ax.set_xlabel('Data', fontsize=14)
    #ax.grid(True, linestyle='--', alpha=1, color='gray')
    ax.set_facecolor(color='whitesmoke')
    ax.tick_params(axis='both', which='major', labelsize=16)

    #borda
    ax.spines['top'].set_color('lightgray')       # Borda superior
    ax.spines['right'].set_color('lightgray')     # Borda direita
    ax.spines['bottom'].set_color('lightgray')    # Borda inferior
    ax.spines['left'].set_color('lightgray')      # Borda esquerda

    # ax.spines['top'].set_linewidth(1)         # Espessura da borda superior

# Correção do Seasonal Decompose e Plots
result = seasonal_decompose(df_diario['Temperatura Média Diária (°C)'], model='additive', period=12)

# Plotar em tamanho maior
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 8))

#result.observed.plot(ax=ax1)
#plot_ax(result.observed, ax)
plot_ax(result.trend, ax1, "Tendência")
plot_ax(result.seasonal, ax2, "Sazonalidade")
plot_ax(result.resid, ax3, "Ruído")

plt.tight_layout()
plt.show()

# %%
