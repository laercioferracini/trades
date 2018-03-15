import sqlite3

conn = sqlite3.connect('trades.db')
cursor = conn.cursor()

def conecta():
    conexao = sqlite3.connect('trades.db')
    return conexao