import os
import requests
from bs4 import BeautifulSoup
import pymysql as pmq
from datetime import datetime
import yagmail
from dotenv import load_dotenv

load_dotenv()
senha_db = os.getenv('senha_db')
email_remetente = os.getenv('email_remetente')
email_destinatario = os.getenv('email_destinatario')
email_senha_app = os.getenv('email_senha_app')

conexao = pmq.connect(
    host = 'localhost',
    user = 'root',
    password = senha_db
)

cursor = conexao.cursor()

cursor.execute("DROP DATABASE IF EXISTS CHOCOLATERIA")

cursor.execute("CREATE DATABASE CHOCOLATERIA")
cursor.execute("USE CHOCOLATERIA")
cursor.execute("CREATE TABLE CHOCOLATES (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, NOME_PRODUTO VARCHAR(255) NOT NULL, PRECO DECIMAL(10,2) NOT NULL, DATA_COLETA DATETIME NOT NULL)""")


hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
hora_email = datetime.now().strftime('%d/%m/%Y %H:%M')

stut = 'https://www.stuttgart.com.br/bomboniere/barras-de-chocolate.html'

resposta = requests.get(stut)
if resposta.status_code != 200:
    raise SystemExit('Erro ao requisitar informações do site.')

stut_site = BeautifulSoup(resposta.text, features='html.parser')

ol_principal = stut_site.find('ol', class_='filterproducts products list items product-items')

produtos = []
for item in ol_principal.find_all('li'):
    nome_tag = item.find('strong', class_ = 'product name product-item-name')
    preco_tag = item.find('div', class_ = 'price-box price-final_price')
    if not nome_tag or not preco_tag:
        continue
    texto_preco = preco_tag.text.strip()
    if not texto_preco:
        continue

    preco = float(
        texto_preco.replace('R$','').replace('.','').replace(',','').strip()
    )

    produtos.append((nome_tag.text.strip(), texto_preco))



query = '''
SELECT COUNT(*) FROM CHOCOLATES
'''
cursor.execute(query)
tem_dados = cursor.fetchone()
if tem_dados[0] > 0:
    query = '''DELETE FROM CHOCOLATES'''
    cursor.execute(query)
for nome,preco in zip(nome_tabela_choc,preco_tabela_choc):
    query = '''
    INSERT INTO CHOCOLATES(NOME_PRODUTO, PRECO, DATA_COLETA) VALUES
    (%s,%s,%s)'''
    valores = [(nome,preco,hora_atual) for nome, preco in produtos]
    cursor.executemany(query, valores)

conexao.commit()

query = '''
SELECT NOME_PRODUTO, PRECO FROM CHOCOLATES
'''
cursor.execute(query)
resultados = cursor.fetchall()
cursor.close()
conexao.close()

corpo_html = '''
<p style="font-size: 1em;">🍫🥚Feliz Páscoa! Veja as ofertas de chocolates Stuttgart</p><table><thead><tr><th>Produtos</th><th>Preço</th></tr></thead><tbody style="font-size: 1em">
'''


for nome,preco in resultados:
    preco_formatado = f'R${preco:.2f}'
    corpo_html += f'''<tr><td>{nome}</td><td style="padding-left: 25px">{preco_formatado.replace(".",",")}</td></tr>'''

html = f'''{corpo_html}</tbody></table><p>⌚ Coleta realizada em: {hora_email}</p><p>Veja mais em: https://www.stuttgart.com.br/bomboniere/barras-de-chocolate.html</p>'''

yag = yagmail.SMTP(email_remetente, email_senha_app)

try:
    yag.send(to=email_destinatario, subject='🐰Ofertas de Páscoa - Chocolates Stuttgart', contents=html)
except Exception as erro:
    print(f'Erro ao enviar o email: {erro}')
