# Previsão de Séries Temporais com ARIMA e Random Forest

Este projeto tem como objetivo realizar a previsão de uma série temporal de quantidade de ligações, utilizando abordagens clássicas (ARIMA) e de aprendizagem de máquina (Random Forest). O foco está em compreender a natureza da série temporal, avaliar sua estacionaridade e desenvolver modelos preditivos eficazes.
Estrutura do Projeto

---

## Carregamento, Preparação e Limpeza de Dados

- Carregar os dados e realizar uma inspeção inicial;
- Resumir os dados, convertendo-os para agregações mensais (ex.: jun/21 = 30);
- Identificar e lidar com valores faltantes.

2. Análise Descritiva
Estatísticas Básicas e Outliers

    Gerar estatísticas descritivas (ex.: média, mediana, desvio-padrão).
    Utilizar diagramas de caixa para identificar e tratar possíveis outliers.

Entendimento da Distribuição

    Plotar histogramas para analisar a distribuição dos dados.
    Gerar um Q-Q Plot para verificar a aderência dos dados à normalidade.

Verificação da Série Temporal

    Visualizar a série para identificar tendências, sazonalidade ou padrões.
    Realizar a decomposição da série em tendência, sazonalidade e resíduos.
    Aplicar transformações como logaritmo e/ou diferenciação (incluindo sazonal) para estabilizar a série.
    Confirmar estacionaridade com plots visuais e estatísticas (ex.: média tendendo a 0).

Análise de Autocorrelação

    Gerar gráficos de Autocorrelação (ACF) e Autocorrelação Parcial (PACF).
    Identificar possíveis parâmetros para modelagem ARIMA.

3. Previsão com ARIMA
Divisão dos Dados

    Separar os dados em conjuntos de treino e teste.

Modelagem e Treinamento

    Aplicar o modelo ARIMA nos dados transformados.
    Avaliar os resultados com base no AIC (quanto menor, melhor).
    Analisar os resíduos do modelo:
        Resíduos devem ter distribuição normal.
        Gráficos ACF e PACF devem estar dentro da faixa de 95% de confiança.

Teste e Validação

    Realizar previsões no conjunto de teste.
    Visualizar os resultados e comparar com os valores reais.
    Avaliar o desempenho usando métricas como MAPE e RMSE.

#4. Previsão com Aprendizado de Máquina (Random Forest)
Divisão dos Dados

    Separar os dados em conjuntos de treino e teste.

Modelagem e Previsões

    Treinar o modelo de Random Forest com os dados de treino.
    Gerar previsões para o conjunto de teste.
    Plotar as previsões junto à série temporal original.
    Avaliar o desempenho usando MAPE e RMSE.

5. Conclusão

    Comparar os resultados dos modelos ARIMA e Random Forest.
    Identificar o modelo mais adequado para os dados.
    Discussão sobre os desafios enfrentados e possíveis melhorias.

Tecnologias Utilizadas

    Python
        pandas, numpy (manipulação e análise de dados)
        matplotlib, seaborn (visualização de dados)
        statsmodels (modelagem ARIMA)
        scikit-learn (Random Forest e métricas de avaliação)
    Jupyter Notebook

Métricas de Avaliação

    MAPE (Mean Absolute Percentage Error): Mede o erro percentual médio absoluto das previsões.
    RMSE (Root Mean Square Error): Mede o erro médio quadrático das previsões.

Contato

    Autor: Alisson Aragão dos Santos
    Email: alissonaragao1@gmail.com
    LinkedIn: https://www.linkedin.com/in/alisson-arag%C3%A3o-dos-santos-459297120/
