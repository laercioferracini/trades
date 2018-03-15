import csv
import sqlite3
# lendo arquivo.
with open('fullOrders.csv', 'rt', newline='') as arquivo:
    header = arquivo.__next__().split(',')

    print(header.__getitem__(1))
    registers = list()
    for linha in csv.reader(arquivo, delimiter=','):
        registers.append(linha)

    print(registers)

    conn = sqlite3.connect('trades.db')
    c = conn.cursor()
    c.execute("""Drop table trades""")

    # criando a tabela
    c.execute('''CREATE TABLE trades 
        (OrderUuid, Exchange, Type, Quantity INTEGER, 'Limit' INTEGER, CommissionPaid INTEGER, Price INTEGER, Opened DATETIME, Closed) ''')

    c.executemany('INSERT INTO TRADES VALUES (?,?,?,?,?,?,?,?,?)', registers)

    conn.commit()

    conn.close()
