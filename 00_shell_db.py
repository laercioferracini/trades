import sqlite3

conn = sqlite3.connect('trades.db')
conn.isolation_level = None
c = conn.cursor()

buffer = ""

print("Digite os comandos SQL para executar no SQLITE3. :)")
print('Para sair entre com uma linha em branco.')

while True:
    line = input()
    if line == "":
        break

    buffer = line
    print('1- ', buffer)

    if sqlite3.complete_statement(buffer):
        print('2 - entrou no if')
        try:
            buffer = buffer.strip()
            c.execute(buffer)
            print('3 - ', buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print(c.fetchall())

        except sqlite3.Error as e:
            print("An error occured: ", e.args[0])
        buffer = ""

conn.close()
