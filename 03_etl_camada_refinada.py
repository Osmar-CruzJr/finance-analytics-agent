# Databricks notebook source
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import DataType, DoubleType

# COMMAND ----------

# cluster spark
spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

# Buscar os dados no database
df_bronze = spark.table('db_analytics.precos_brutos_bitcoin').toPandas()
type(df_bronze)

# COMMAND ----------

# Verificar
print(df_bronze.shape)
print(df_bronze.dtypes)
df_bronze.sample(5)

# COMMAND ----------

# Converter o campo data
df_bronze['data'] = pd.to_datetime(df_bronze['data'])

# COMMAND ----------

# Transformando o perído inicial da semanas
df_bronze['semana_inicio'] = df_bronze['data'].dt.to_period('w').apply(lambda x: x.start_time)

df_bronze.head()

# COMMAND ----------

# Análise quantidade de dias em cada semana
df_bronze.semana_inicio.value_counts().sort_index()

# COMMAND ----------

# Agrupamento por semana
df_gold = df_bronze.groupby(['semana_inicio']).agg(semana_fim=('data', 'max'),
                                         abertura=('abertura', 'first'),
                                          maximo=('maximo', 'max'),
                                          minimo=('minimo', 'min'),
                                          fechamento=('fechamento', 'last'),
                                          volume_medio=('volume', 'mean')).reset_index()
df_gold.head()


# COMMAND ----------

# Calcular a variacao percentual
df_gold['variacao_pct'] = (df_gold['fechamento'] - df_gold['abertura']) / df_gold['abertura'] * 100
df_gold.head()

# COMMAND ----------

# Converter os campos de datas
df_gold['semana_inicio'] = pd.to_datetime(df_gold['semana_inicio']).dt.date
df_gold['semana_fim'] = pd.to_datetime(df_gold['semana_fim']).dt.date 

# COMMAND ----------

# Converter df pandas para spark
df_spark = spark.createDataFrame(df_gold)
df_spark.write.format('delta').mode('overwrite').saveAsTable('db_analytics.precos_semanal_bitcoin')

print(f'Total de semanas processadas: {df_spark.count()}')