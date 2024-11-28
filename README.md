# Análise e Modelagem de Séries Temporais: Previsão de Chamadas de um Call Center com ARIMA e Random Forest

Este projeto tem como objetivo realizar a previsão de uma série temporal de quantidade de ligações, utilizando abordagens clássicas (ARIMA) e de aprendizagem de máquina (Random Forest). O foco está em compreender a natureza da série temporal, avaliar sua estacionaridade e desenvolver modelos preditivos eficazes.
Estrutura do Projeto

---

## Estrutura do Repositório

```plaintext
├── documentacao  
|   ├── .gitkeep                            # Arquivo para manter diretórios vazios no repositório Git
|   ├── dicionario_base.pdf                  # Dicionário de dados detalhando o conjunto utilizado no projeto
|
│                                          
├── src                                     # Diretório principal com scripts de ETL e análise
│   ├── analysis
│   │   └── analise_e_previsao.ipynb        # Notebook com a análise exploratória e modelagem
│   ├── etl
│   │   ├── 01_ingestao_carga_historica.py  # Script para ingestão inicial de dados históricos
│   │   ├── 02_ingestao_diaria.py           # Script para ingestão diária de dados
│   │   ├── 03_ingestao_silver.py           # Script para transformação e padronização dos dados (camada Silver)
│   │   ├── ingestao_silver.sql             # SQL para suporte às transformações da camada Silver
│   │   └── inserir_dt_processamento.sql    # SQL para registrar a data de processamento
├── .gitignore                              # Arquivo para especificar arquivos/diretórios a serem ignorados no Git
├── README.md                               # Documentação principal do projeto
```
---

## Escopo de Projeto

### 1. Carregamento, Preparação e Limpeza de Dados

Fluxo de tranformação:

![image](https://github.com/user-attachments/assets/e8990536-f8b8-4675-a299-c86ab5961454)

---

### 2. Análise Descritiva

- Estatísticas e distribuição dos dados;
- Verificação da Série Temporal;
- Análise de Autocorrelação.

### 3. Previsão com ARIMA

- Aplicar o modelo ARIMA nos dados transformados;
- Avaliar os resultados com base no AIC (quanto menor, melhor);
- Analisar os resíduos do modelo (resíduos devem ter distribuição normal dentro da faixa de 95% de confiança).

### 4. Previsão com Aprendizado de Máquina (Random Forest)

- Divisão dos Dados conjuntos de treino e teste;
- Treinar o modelo de Random Forest com os dados de treino;
- Gerar previsões para o conjunto de teste;
- Plotar as previsões junto à série temporal original;
- Avaliar o desempenho usando MAPE e RMSE.

### 5. Conclusão

- Comparar os resultados dos modelos ARIMA e Random Forest;
- Identificar o modelo mais adequado para os dados;
- Discussão sobre os desafios enfrentados e possíveis melhorias.

---

### Métricas de Avaliação Utilizadas

- MAPE (Mean Absolute Percentage Error): Mede o erro percentual médio absoluto das previsões;
- RMSE (Root Mean Square Error): Mede o erro médio quadrático das previsões.

---

## Tecnologias Utilizadas

- **Jupyter Notebook**: Ambiente interativo utilizado para execução do código e visualização dos resultados
- **BigQuery**: Ambiente na cloud da Google para armazenar, consultar e analisar grandes volumes de dados
- **Python 3.12.2**: Linguagem de Programação utilizada
  - **Pandas**: Para manipulação e organização dos dados
  - **Scikit-learn**: Para criação e treinamento do modelo Random Forest
  - **Statsmodels**: Para criação e treinamento do modelo ARIMA
  - **Matplotlib**: Para visualizações gráficas
  - **Requests**: Realizar requisições HTTP para APIs ou serviços web
  - **Google.cloud**: Integração com o Google BigQuery para consultas e manipulação de dados
  - **Pyspark**: Interface Python para o Apache Spark, usada para processamento de grandes volumes de dados de forma distribuída

---

## Contato

Autor: Alisson Aragão dos Santos

Email: alissonaragao1@gmail.com

LinkedIn: [alisson-aragão-dos-santos](https://www.linkedin.com/in/alisson-arag%C3%A3o-dos-santos-459297120/)
