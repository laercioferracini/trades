import sqlite3

"""
# cursor.execute("SELECT DISTINCT Exchange FROM TRADES ")
# r = cursor.fetchall()
# len(r) retorna o número de linhas na query
# cursor.execute("SELECT DISTINCT Exchange FROM TRADES ORDER BY Exchange")
# Colunas ['OrderUuid', 'Exchange', 'Type', 'Quantity', 'Limit', 'CommissionPaid', 'Price', 'Opened', 'Closed']
# cursor.execute("SELECT * FROM TRADES")

"""
conn = sqlite3.connect('trades.db',  detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()

market = ('BTC-MUSIC', 'LIMIT_BUY')

cursor.execute("SELECT price FROM trades WHERE Exchange LIKE ? AND Type LIKE ?", market)

#lista = cursor.fetchall()
total = 0
#print(lista.__str__().replace(',', '').replace('(', '').replace(')', ''))

total = [float(linha[0]) for linha in cursor.fetchall()]

    #print('O valor é {0} datatype é {1}'.format(linha, type(linha)))
    #print(linha)

print(total)
sum = 0
sum += float(total[0])
sum += float(total[1])
sum += float(total[2])
sum += float(total[3])

print(sum)

conn.commit()

conn.close()
