# Análise e Modelagem de Séries Temporais: Previsão de Chamadas de um Call Center com ARIMA e Random Forest

Este projeto tem como objetivo realizar a previsão de uma série temporal de quantidade de ligações, utilizando abordagens clássicas (ARIMA) e de aprendizagem de máquina (Random Forest). O foco está em compreender a natureza da série temporal, avaliar sua estacionaridade e desenvolver modelos preditivos eficazes.
Estrutura do Projeto

---

## Escopo de Projeto

### Carregamento, Preparação e Limpeza de Dados

- Carregar os dados e realizar uma inspeção inicial;
- Resumir os dados, convertendo-os para agregações mensais (ex.: jun/21 = 30);
- Identificar e lidar com valores faltantes.

---

### Análise Descritiva

Estatísticas e distribuição dos dados:
- Gerar estatísticas descritivas (ex.: média, mediana, desvio-padrão);
- Utilizar diagramas de caixa para identificar e tratar possíveis outliers;
- Plotar histogramas para analisar a distribuição dos dados;
- Gerar um Q-Q Plot para verificar a aderência dos dados à normalidade.
 
Verificação da Série Temporal:
- Visualizar a série para identificar tendências, sazonalidade ou padrões;
- Realizar a decomposição da série em tendência, sazonalidade e resíduos;
- Aplicar transformações como logaritmo e/ou diferenciação (incluindo sazonal) para estabilizar a série;
- Verificar estacionaridade com plots visuais e estatísticas (ex.: média tendendo a 0).

Análise de Autocorrelação
- Gerar gráficos de Autocorrelação (ACF) e Autocorrelação Parcial (PACF);
- Identificar possíveis parâmetros para modelagem ARIMA.

---

### Previsão com ARIMA

Modelagem e Treinamento:
- Divisão dos Dados em conjuntos de treino e teste;
- Aplicar o modelo ARIMA nos dados transformados;
- Avaliar os resultados com base no AIC (quanto menor, melhor).

Analisar os resíduos do modelo:
- Resíduos devem ter distribuição normal;
- Gráficos ACF e PACF devem estar dentro da faixa de 95% de confiança.

Teste e Validação:
- Realizar previsões no conjunto de teste;
- Visualizar os resultados e comparar com os valores reais;
- Avaliar o desempenho usando métricas como MAPE e RMSE.

---

### Previsão com Aprendizado de Máquina (Random Forest)

Modelagem e Previsões
- Divisão dos Dados conjuntos de treino e teste;
- Treinar o modelo de Random Forest com os dados de treino;
- Gerar previsões para o conjunto de teste;
- Plotar as previsões junto à série temporal original;
- Avaliar o desempenho usando MAPE e RMSE.

---

## Conclusão

- Comparar os resultados dos modelos ARIMA e Random Forest;
- Identificar o modelo mais adequado para os dados;
- Discussão sobre os desafios enfrentados e possíveis melhorias.

---

### Métricas de Avaliação

- MAPE (Mean Absolute Percentage Error): Mede o erro percentual médio absoluto das previsões;
- RMSE (Root Mean Square Error): Mede o erro médio quadrático das previsões.

---

## Tecnologias Utilizadas

- **Python**
- **Pandas**: Para manipulação e organização dos dados;
- **Scikit-learn**: Para criação e treinamento do modelo Random Forest;
- **Statsmodels**: Para criação e treinamento do modelo ARIMA;
- **Matplotlib**: Para visualizações gráficas;
- **Jupyter Notebook**: Ambiente interativo utilizado para execução do código e visualização dos resultados.

---

## Distribuição do Projeto

├── src 
|   ├── .gitkeep                   # Arquivo para manter diretórios vazios no repositório Git
|   ├── Citizen_Service_Request__CSR__Call_Center_Calls_-_Data_Dictionary.pdf  
├── src                            # Diretório principal com scripts de ETL e análise
│   ├── analysis
│   │   └── analise_e_previsao.ipynb # Notebook com a análise exploratória e previsões da série temporal
│   ├── etl
│   │   ├── 01_ingestao_carga_historica.py  # Script para ingestão inicial de dados históricos
│   │   ├── 02_ingestao_diaria.py           # Script para ingestão diária de dados
│   │   ├── 03_ingestao_silver.py           # Script para transformação e padronização dos dados (camada Silver)
│   │   ├── ingestao_silver.sql             # SQL para suporte às transformações da camada Silver
│   │   └── inserir_dt_processamento.sql    # SQL para registrar a data de processamento
├── .gitignore                     # Arquivo para especificar arquivos/diretórios a serem ignorados no Git
├── README.md                      # Documentação principal do projeto

---

## Contato

Autor: Alisson Aragão dos Santos

Email: alissonaragao1@gmail.com

LinkedIn: [alisson-aragão-dos-santos](https://www.linkedin.com/in/alisson-arag%C3%A3o-dos-santos-459297120/)
