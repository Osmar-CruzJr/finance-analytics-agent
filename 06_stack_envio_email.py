# Databricks notebook source
# MAGIC %pip install resend --quiet

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

html = '''

<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Relatório Executivo de Mercado: Bitcoin (BTC)</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f1f5f9; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased; color: #0f172a;">

  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f1f5f9; padding: 30px 0;">
    <tr>
      <td align="center">
        <!-- Main Email Container -->
        <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);">
          
          <!-- Header -->
          <tr>
            <td style="background-color: #0f172a; padding: 32px 40px; text-align: left;">
              <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <tr>
                  <td>
                    <span style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 1.2px; display: block; margin-bottom: 6px;">Pesquisa de Criptoativos & Microestrutura</span>
                    <h1 style="margin: 0; font-size: 20px; color: #ffffff; font-weight: 700; line-height: 1.3;">RELATÓRIO EXECUTIVO: BITCOIN (BTC)</h1>
                  </td>
                </tr>
                <tr>
                  <td style="padding-top: 16px; border-top: 1px solid #1e293b; margin-top: 16px;">
                    <p style="margin: 0; font-size: 12px; color: #94a3b8; line-height: 1.5;">
                      <strong>Para:</strong> Diretoria de Investimentos / Mesa de Trading<br>
                      <strong>Período:</strong> Semana 24-30/Ago vs. Semana 31/Ago-04/Set (2026)
                    </p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Executive Summary -->
          <tr>
            <td style="padding: 32px 40px 24px 40px;">
              <h2 style="margin: 0 0 16px 0; font-size: 14px; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; text-transform: uppercase; letter-spacing: 0.8px;">1. Resumo Executivo</h2>
              <p style="margin: 0 0 20px 0; font-size: 14px; line-height: 1.6; color: #334155;">
                Após uma semana de forte consolidação (W-1), o Bitcoin apresentou expansão de volatilidade e fechamento positivo na última semana (W-0), rompendo a estrutura anterior.
              </p>
              
              <!-- Metrics Cards -->
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-bottom: 12px;">
                <tr>
                  <td width="48%" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px; vertical-align: top;">
                    <div style="font-size: 11px; text-transform: uppercase; color: #64748b; font-weight: 600; letter-spacing: 0.5px;">Variação de Preço</div>
                    <div style="font-size: 22px; font-weight: 700; color: #16a34a; margin: 6px 0 2px 0;">+4,65%</div>
                    <div style="font-size: 12px; color: #64748b;">$77.667,60 &rarr; $81.278,10</div>
                  </td>
                  <td width="4%"></td>
                  <td width="48%" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 16px; vertical-align: top;">
                    <div style="font-size: 11px; text-transform: uppercase; color: #64748b; font-weight: 600; letter-spacing: 0.5px;">Volume Médio Diário</div>
                    <div style="font-size: 22px; font-weight: 700; color: #dc2626; margin: 6px 0 2px 0;">-3,27%</div>
                    <div style="font-size: 12px; color: #64748b;">$34,05B &rarr; $32,93B</div>
                  </td>
                </tr>
              </table>

              <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <tr>
                  <td style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px 16px; font-size: 12px; color: #475569;">
                    <strong>Extremos Semanais:</strong> Mínima em <strong>US$ 76.248,30</strong> <em>(varrida de liquidez)</em> | Máxima em <strong>US$ 81.392,30</strong> <em>(teste de topo)</em>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Highlights of the Week -->
          <tr>
            <td style="padding: 8px 40px 24px 40px;">
              <h2 style="margin: 0 0 16px 0; font-size: 14px; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; text-transform: uppercase; letter-spacing: 0.8px;">2. Destaques da Semana</h2>
              
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-bottom: 16px;">
                <tr>
                  <td style="padding-bottom: 12px;">
                    <strong style="color: #0f172a; font-size: 13px; text-transform: uppercase; letter-spacing: 0.3px;">Tendência Dominante</strong>
                    <p style="margin: 4px 0 0 0; font-size: 14px; color: #334155; line-height: 1.5;">
                      <strong>Alta de Curto Prazo (Expansão Alta):</strong> O mercado rompeu a faixa lateral (~US$ 76,6k–81,3k) buscando liquidez acima do topo anterior e fechando próximo da máxima semanal.
                    </p>
                  </td>
                </tr>
                <tr>
                  <td>
                    <strong style="color: #0f172a; font-size: 13px; text-transform: uppercase; letter-spacing: 0.3px;">Microestrutura & Confirmação por Volume</strong>
                    <p style="margin: 4px 0 0 0; font-size: 14px; color: #334155; line-height: 1.5;">
                      <strong style="color: #d97706;">Divergência de Exaustão (Alerta):</strong> A alta com volume declinante (-3,27%) sugere um movimento impulsionado por <em>short squeeze</em> ou livros de ofertas rasos (<em>thin order book</em>), e não por acumulação institucional consistente no mercado <em>spot</em>.
                    </p>
                  </td>
                </tr>
              </table>

              <!-- Critical Levels Box -->
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f1f5f9; border-left: 4px solid #2563eb; border-radius: 0 6px 6px 0;">
                <tr>
                  <td style="padding: 16px;">
                    <div style="font-weight: 700; font-size: 12px; color: #1e40af; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px;">Mapeamento de Níveis Críticos</div>
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="font-size: 13px; color: #334155;">
                      <tr>
                        <td style="padding: 3px 0;">Resistência Macro</td>
                        <td align="right" style="font-weight: 700; color: #0f172a;">US$ 83.500</td>
                      </tr>
                      <tr>
                        <td style="padding: 3px 0;">Resistência Imediata</td>
                        <td align="right" style="font-weight: 700; color: #0f172a;">US$ 81.400</td>
                      </tr>
                      <tr>
                        <td style="padding: 3px 0;">Suporte Imediato (Pivot)</td>
                        <td align="right" style="font-weight: 700; color: #0f172a;">US$ 77.670</td>
                      </tr>
                      <tr>
                        <td style="padding: 3px 0;">Suporte Crítico</td>
                        <td align="right" style="font-weight: 700; color: #0f172a;">US$ 76.250</td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Points of Attention -->
          <tr>
            <td style="padding: 8px 40px 24px 40px;">
              <h2 style="margin: 0 0 16px 0; font-size: 14px; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; text-transform: uppercase; letter-spacing: 0.8px;">3. Pontos de Atenção & Gestão de Risco</h2>
              
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="font-size: 14px; color: #334155; line-height: 1.5;">
                <tr>
                  <td width="20" vertical-align="top" style="padding-bottom: 12px; font-weight: 700; color: #dc2626;">1.</td>
                  <td style="padding-bottom: 12px;">
                    <strong>Rejeição em Topo Duplo:</strong> Falha em sustentar o preço acima de US$ 81.400 com expansão de volume confirmará topo duplo, elevando o risco de um <em>fakeout</em> (falso rompimento).
                  </td>
                </tr>
                <tr>
                  <td width="20" vertical-align="top" style="padding-bottom: 12px; font-weight: 700; color: #dc2626;">2.</td>
                  <td style="padding-bottom: 12px;">
                    <strong>Perda da Região Pivot (US$ 77.670):</strong> Um fechamento diário abaixo deste nível anula o cenário autoral de alta e abre caminho para testar o suporte em US$ 76.250.
                  </td>
                </tr>
                <tr>
                  <td width="20" vertical-align="top" style="font-weight: 700; color: #dc2626;">3.</td>
                  <td>
                    <strong>Divergência em Finais de Semana:</strong> Avanços sem liquidez do mercado institucional americano (CME/ETFs) tendem a ser devolvidos na abertura das sessões regulares.
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Tactical Conclusion -->
          <tr>
            <td style="padding: 8px 40px 32px 40px;">
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 6px;">
                <tr>
                  <td style="padding: 20px;">
                    <div style="font-size: 11px; font-weight: 700; color: #1e40af; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 4px;">Conclusão Tática</div>
                    <div style="font-size: 15px; font-weight: 700; color: #1e3a8a; margin-bottom: 8px;">Viés: Neutro a Moderadamente Bullish (Aguardar Confirmação)</div>
                    <p style="margin: 0; font-size: 13px; line-height: 1.6; color: #1e3a8a;">
                      O movimento de alta é válido pela ação do preço, contudo a divergência de volume recomenda cautela antes de novas entradas compradas no topo da faixa. Sugere-se aguardar o reteste de US$ 81.400 com volume comprador ou buscar melhores assimetrias próximo ao suporte de US$ 77.670.
                    </p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color: #f8fafc; border-top: 1px solid #e2e8f0; padding: 24px 40px; text-align: center;">
              <p style="margin: 0 0 8px 0; font-size: 11px; color: #64748b; font-weight: 600;">
                Elaborado por Pesquisa de Criptoativos & Microestrutura de Mercado
              </p>
              <p style="margin: 0; font-size: 10px; color: #94a3b8; line-height: 1.4;">
                <strong>Disclaimer:</strong> Este documento possui caráter estritamente informativo e destina-se exclusivamente ao uso interno da Mesa de Trading e Diretoria de Investimentos. As análises não constituem oferta ou solicitação de compra/venda de ativos financeiros.
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>

</body>
</html>
'''

# COMMAND ----------

import resend
import os
from dotenv import load_dotenv

load_dotenv()

# COMMAND ----------

# Chave da API do Resend
resend.api_key = os.getenv('RESEND_API_KEY')

# COMMAND ----------

html = dbutils.jobs.taskValues.get(taskKey='agente_email', key='html')
type(html)

# COMMAND ----------

# Extrai o HTML da posição [0]['text'] se for uma lista com dicionário
if isinstance(html, list) and len(html) > 0 and isinstance(html[0], dict):
    html_string = html[0].get('text', '')
elif isinstance(html, str):
    html_string = html
else:
    html_string = str(html)

# COMMAND ----------

# Criar o e-mail
params = {
    'from' : 'BTC Analytics <onboarding@resend.dev>',
    'to' : os.getenv('EMAIL_DESTINO'),
    'subject' : 'Relatório Estratégico - BTC',
    'html' : html_string
}

# COMMAND ----------

print(os.getenv('EMAIL_DESTINO'))
print(os.getenv('RESEND_API_KEY'))

# COMMAND ----------

# DBTITLE 1,Cell 7
resposta = resend.Emails.send(params)
print(f'E-mail enviado com Sucesso! {resposta}')