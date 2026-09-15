# Databricks notebook source
# MAGIC %pip install langchain-google-genai python-dotenv tabulate delta-spark --quiet

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

# Copiando o output do agente anterior
analise = '''
# RELATÓRIO EXECUTIVO DE MERCADO: BITCOIN (BTC)
**Para:** Diretoria de Investimentos / Mesa de Trading  
**Elaborado por:** Pesquisa de Criptoativos & Microestrutura de Mercado  
**Período de Análise:** Semana 24-30/Ago vs. Semana 31/Ago-04/Set (2026)

---

### 1. VISÃO GERAL & MÉTRICAS-CHAVE

Após uma semana de forte consolidação (W-1), o Bitcoin apresentou expansão de volatilidade e fechamento positivo na última semana (W-0), rompendo a consolidação anterior.

* **Variação de Preço (Fechamento W-1 vs. W-0):** **+4,65%** (de US$ 77.667,60 para US$ 81.278,10).
* **Variação de Volume Médio Diário:** **-3,27%** (de US$ 34,05 bilhões para US$ 32,93 bilhões).
* **Extremos da Mínima (Lows):** US$ 76.248,30 (W-0) vs. US$ 76.688,80 (W-1) — *Varrida de liquidez na mínima*.
* **Extremos da Máxima (Highs):** US$ 81.392,30 (W-0) vs. US$ 81.347,00 (W-1) — *Teste e rompimento pontual de topo*.

---

### 2. ANÁLISE ESTRUTURAL & TENDÊNCIA

* **Tendência Dominante:** **Alta de Curto Prazo (Expansão Alta).** O mercado saiu de uma estrutura lateral (alcance estreito de ~US$ 76,6k–81,3k) para buscar liquidez acima do topo anterior, fechando próximo da máxima semanal.
* **Microestrutura & Confirmação por Volume:** **Divergência de Exaustão (Alerta).** Embora o preço tenha subido +4,64%, o volume financeiro médio caiu -3,27%. Do ponto de vista de microestrutura, essa alta com volume declinante sugere impulso movido por *short squeeze* ou liquidez fraca nos livros de ofertas (*thin order book*), e não por acumulação institucional agressiva no mercado à vista (*spot*).
* **Mapeamento de Níveis Críticos:**
  * **Resistência Imediata:** **US$ 81.400** (Região de topo duplo recente / Liquidez compradora).
  * **Resistência Macro:** **US$ 83.500** (Projeção de expansão de Fibonacci do movimento).
  * **Suporte Imediato (Pivot):** **US$ 77.670** (Região de abertura/fechamento das duas últimas semanas).
  * **Suporte Crítico:** **US$ 76.250** (Mínima da semana atual / Fundo de liquidez).

---

### 3. PONTOS DE ATENÇÃO & GESTÃO DE RISCO

1. **Rejeição em Topo Duplo (Falha de Breakout):** A incapacidade de sustentar o preço acima de US$ 81.400 com volume comprador crescente nas primeiras sessões da próxima semana confirmará uma formação de topo duplo, aumentando a probabilidade de um *fakeout* (falso rompimento).
2. **Perda da Região Pivot (US$ 77.670):** O retorno e fechamento diário abaixo deste nível anula a estrutura autoral de alta e reabre espaço para retestar a liquidez compradora em US$ 76.250.
3. **Divergência de Volume em Finais de Semana:** Movimentos de continuidade iniciados sem volume de suporte do mercado institucional americano (CME/ETFs) tendem a ser devolvidos no início das sessões normais de negociação.

---

### 4. CONCLUSÃO TÁTICA

**Viés para a próxima semana:** **Neutro a Moderadamente Bullish (Aguardar Confirmação).** 

O movimento de alta estrutural do BTC é válido pelo preço, porém a divergência de volume exige cautela antes de montagens de posições compradas no topo da faixa. Recomendamos aguardar o reteste do nível de US$ 81.400 acompanhado de expansão de volume ou buscar entradas de melhor risco/retorno próximo ao suporte de US$ 77.670.
'''

# COMMAND ----------

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Carregar o enviroment
load_dotenv()

# COMMAND ----------

# Ler o prompt
with open('prompts/agente_html.txt') as file:
    prompt_template = file.read()


# COMMAND ----------

# Receber do JOB a informação do outro agente
analise = dbutils.jobs.taskValues.get(taskKey='agente_analise', key='analise')

# COMMAND ----------

prompt = prompt_template.replace('{analise}', analise)

# COMMAND ----------

# Chamando Gemini
llm = ChatGoogleGenerativeAI(model='gemini-3.6-flash', google_api_key=os.getenv('GOOGLE_API_KEY'))
llm

# COMMAND ----------

resposta = llm.invoke(prompt)
html = resposta.content
print(html)

# COMMAND ----------

dbutils.jobs.taskValues.set(key='html', value=html)