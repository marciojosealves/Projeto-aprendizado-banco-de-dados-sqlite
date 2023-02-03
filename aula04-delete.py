import sqlite3

banco = sqlite3.connect("banco-escolar.db")

cursor = banco.cursor()

# normalmente é utilizado ID
cursor.execute("DELETE FROM alunos WHERE contato = 9911111111")

banco.commit()

banco.close()
