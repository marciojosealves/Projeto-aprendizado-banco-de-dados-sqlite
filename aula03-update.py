import sqlite3

banco = sqlite3.connect("banco-escolar.db")

cursor = banco.cursor()

# UPDATE é utilizado por um ID,  identificação única... "WHERE ID = id"
cursor.execute(
    "UPDATE alunos SET nome = 'marcio jose alves', idade = 99, contato = 9912345678 WHERE curso = 'engenharia' ")

banco.commit()

banco.close()
