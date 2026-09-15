# Databricks notebook source
# instalando o pacote Yfinance
!pip install yfinance --quiet

# COMMAND ----------

# imports
import yfinance as yf
import pandas as pd

# COMMAND ----------

# parâmetros para consumir API da Yfinance
ticker = 'BTC-USD'
periodo = '1y'
intervalo = '1d'

# carregar dados da API
dados_brutos = yf.download(ticker, period=periodo, interval=intervalo)
# visualizar dados
display(dados_brutos)


# COMMAND ----------

dados_brutos.columns

# COMMAND ----------

# formatar os dados
dados_brutos = dados_brutos.reset_index()
dados_brutos.columns = [coluna[0].lower() for coluna in dados_brutos.columns]
dados_brutos.head()

# COMMAND ----------

# renomear colunas
dados_brutos.rename(columns={
    'date': 'data', 
    'open': 'abertura', 
    'high': 'maximo', 
    'low': 'minimo', 
    'close': 'fechamento', 
    'volume': 'volume'
}, inplace=True)

# COMMAND ----------

dados_brutos.dtypes

# COMMAND ----------

# ingestão dos dados
from pyspark.sql import SparkSession

#cluster (iniciar o Spark)
spark = SparkSession.builder.getOrCreate()
spark

# COMMAND ----------

# tratamento para garantir formatos na tabela
dados_brutos['data']      = pd.to_datetime(dados_brutos['data']).dt.date
dados_brutos['abertura']  = dados_brutos['abertura'].astype(float)
dados_brutos['maximo']    = dados_brutos['maximo'].astype(float)
dados_brutos['minimo']    = dados_brutos['minimo'].astype(float)
dados_brutos['fechamento'] = dados_brutos['fechamento'].astype(float)
dados_brutos['volume']    = dados_brutos['volume'].astype(float)

# COMMAND ----------

# converter o df pandas para Spark
df_spark = spark.createDataFrame(dados_brutos)

#ingestçao no db SQL
df_spark.write.format('delta').mode('overwrite').saveAsTable('db_analytics.precos_brutos_bitcoin')

print(f'Total de {df_spark.count()} linhas gravadas')