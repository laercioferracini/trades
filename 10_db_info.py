import sqlite3

conn = sqlite3.connect('trades.db')
c = conn.cursor()
nome_tabela = 'trades'
#Colunas ['OrderUuid', 'Exchange', 'Type', 'Quantity', 'Limit', 'CommissionPaid', 'Price', 'Opened', 'Closed']
#PEGA INFORMAÇÕES DA TABELA
c.execute('PRAGMA table_info({})'.format(nome_tabela))

colunas = [tupla[1] for tupla in c.fetchall()]

print('Colunas', colunas)

#listando as tabelas do bd
c.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY NAME""")

print('Tabelas:')
for tabela in c.fetchall():
    print("%s" % (tabela))

# obtendo o schemada tabela
c.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""", (nome_tabela,))

print('Schema: ')

for schema in c.fetchall():
    print("%s" % (schema))

conn.close()