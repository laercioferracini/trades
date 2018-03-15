import sqlite3

conn = sqlite3.connect('trades.db')

cursor = conn.cursor()
# cursor.execute("""Drop table TRADES""")
# #criando a tabela
# cursor.execute('''CREATE TABLE TRADES
#     (OrderUuid, Exchange, Type, Quantity, 'Limit', CommissionPaid, Price, Opened, Closed) ''')
# cursor.execute("INSERT INTO TRADES VALUES ('6cd6613c-04fc-41ab-83d5-1f92b60ae061','BTC-MUSIC','LIMIT_BUY','527.77777778',"
#                "'0.00000189','0.00000249','0.00099750','2/22/2018 1:25:49 AM','2/22/2018 1:31:43 AM') ")

print(cursor.fetchone())
p = ('BTC-MUSIC',)
cursor.execute("SELECT * FROM TRADES WHERE Exchange like 'BTC-MUSIC' ")

for linha in cursor.fetchall():
    print(linha)

conn.commit()

conn.close()
