# Databricks notebook source
# MAGIC %pip install langchain-google-genai python-dotenv tabulate delta-spark --quiet

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI 
from pyspark.sql import SparkSession

# COMMAND ----------

# Leitura do arquivo env
load_dotenv()

# Criando Cluster spark
spark = SparkSession.builder.appName("Spark").getOrCreate()

# COMMAND ----------

# Leitura de dados
df_gold = spark.table('db_analytics.precos_semanal_bitcoin').orderBy('semana_inicio', ascending=False).limit(2).toPandas() 

df_gold

# COMMAND ----------

# Melhorando a visualização para o agente
dados_formatados = df_gold.to_markdown(index=False)
dados_formatados

# COMMAND ----------

# Criando Prompt
with open('prompts/agente_analise.txt') as arquivo:
    prompt = arquivo.read()
    
prompt

# COMMAND ----------

# Incluir a informação no prompt
prompt_final = prompt.replace('{dados_semanal}', dados_formatados)
prompt_final

# COMMAND ----------

# Chamando Gemini
llm = ChatGoogleGenerativeAI(model='gemini-3.6-flash', google_api_key=os.getenv('GOOGLE_API_KEY'))
llm

# COMMAND ----------

# Enviar o prompt
resposta = llm.invoke(prompt_final)


# COMMAND ----------

# Recebendo resposta
analise = resposta.content[0]['text']
print(analise)

# COMMAND ----------

# Utilizando a saída da análise para levar ao agente construtor de email
dbutils.jobs.taskValues.set(key='analise', value=analise)