
CREATE TABLE project-tcc-434118.SILVER_ATD_CSR.tb_interacao_receptivo
AS
SELECT
   CAST(UNIQUE_ID AS INT64) AS registroId
  ,CAST(AGENTDISPID AS INT64) AS agenteDispId
  ,CAST(
    CASE 
      WHEN INSTR(LEFT(CALLSTARTDT, 10), '/') > 0 
      THEN CONCAT(
        RIGHT(REPLACE(LEFT(CALLSTARTDT, 10), '/', ''), 4),
        '-',
        LEFT(REPLACE(LEFT(CALLSTARTDT, 10), '/', ''), 2),
        '-',
        SUBSTRING(REPLACE(LEFT(CALLSTARTDT, 10), '/', ''), 3, 2)
      )
      ELSE LEFT(CALLSTARTDT, 10) 
    END
   AS DATE) AS dtChamada
  ,CAST(CALLACTIONID       AS INT64) AS acaoChamadaId 
  ,CAST(CALLACTIONREASONID AS INT64) AS acaoMotivoChamadaId
  ,CAST(CALLID             AS INT64) AS chamadaId

  -- Conversão para dtEncerramentoConnHora
   ,COALESCE(
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%E*3S', CONNCLEARDT)), 'America/New_York'),
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%m/%d/%Y %H:%M:%S %p', CONNCLEARDT)), 'America/New_York'),
    CAST(CONNCLEARDT AS DATETIME)
   ) AS dtEncerramentoConnHora

  -- ,CAST(DNIS AS INT64) AS numeroDiscagem

  -- Conversão para dtEntradaFilaHora
  ,COALESCE(
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%E*3S', QUEUESTARTDT)), 'America/New_York'),
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%m/%d/%Y %H:%M:%S %p', QUEUESTARTDT)), 'America/New_York'),
    CAST(QUEUESTARTDT AS DATETIME)
   ) AS dtEntradaFilaHora

  ,CAST(SEQNUM        AS INT64) AS numSequencial
  ,CAST(SERVICE_ID    AS INT64) AS servicoId
  ,CAST(STATION       AS INT64) AS estacao
  ,CAST(WORKGROUP_ID  AS INT64) AS grupoTrabalhoId

  -- Conversão para dtTerminoEncerramento
  ,COALESCE(
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%E*3S', WRAPENDDT)), 'America/New_York'),
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%m/%d/%Y %H:%M:%S %p', WRAPENDDT)), 'America/New_York'),
    CAST(WRAPENDDT AS DATETIME)
   ) AS dtTerminoEncerramento

  -- Conversão para dtInicioPreVisualizacao
  ,COALESCE(
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%E*3S', PREVIEWSTARTDT)), 'America/New_York'),
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%m/%d/%Y %H:%M:%S %p', PREVIEWSTARTDT)), 'America/New_York'),
    CAST(PREVIEWSTARTDT AS DATETIME)
   ) AS dtInicioPreVisualizacao

  -- Conversão para dtFimPreVisualizacao
  ,COALESCE(
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%E*3S', PREVIEWENDDT)), 'America/New_York'),
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%m/%d/%Y %H:%M:%S %p', PREVIEWENDDT)), 'America/New_York'),
    CAST(PREVIEWENDDT AS DATETIME)
   ) AS dtFimPreVisualizacao

  -- Conversão para dtResposta
  ,COALESCE(
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%E*3S', ANSWERDT)), 'America/New_York'),
    DATETIME(TIMESTAMP(SAFE.PARSE_TIMESTAMP('%m/%d/%Y %H:%M:%S %p', ANSWERDT)), 'America/New_York'),
    CAST(ANSWERDT AS DATETIME)
   ) AS dtResposta

  ,CAST(ANSWER_SPEED_SECS AS INT64) AS tempoRespostaSeg
  ,CAST(TALK_TIME_SECS  AS INT64) AS tempoConversaSeg
  ,CAST(WRAP_TIME_SECS  AS INT64) AS tempoEncerramentoSeg

  ,CASE 
    WHEN SERVICE_LEVEL = 'Y' THEN 1 
    WHEN SERVICE_LEVEL = 'N' THEN 0 
    ELSE NULL 
   END AS nivelServico

  ,CASE 
    WHEN ABANDONED = 'Y' THEN 1 
    WHEN ABANDONED = 'N' THEN 0 
    ELSE NULL 
   END AS statusAbandono

  ,CASE 
    WHEN ANSWERED = 'Answered' THEN 1 
    WHEN ANSWERED = 'Not Answered' THEN 0 
    ELSE NULL 
   END AS statusChamada

  ,DT_PROCESSAMENTO AS dtProcessamento

FROM `project-tcc-434118.BRONZE_ATD_CSR.tb_interactions`

WHERE 1=1
AND CALLTYPEID = '1'
