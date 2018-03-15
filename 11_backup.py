# 11_backup.py
import sqlite3
import io

conn = sqlite3.connect('trades.db')

with io.open('trades_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)

print('Backup realizado .')
print('Arquivo trades_dump.sql criado corretamente')

conn.close()