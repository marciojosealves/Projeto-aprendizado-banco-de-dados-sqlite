import sqlite3

banco = sqlite3.connect("banco-escolar.db")

cursor = banco.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS alunos(nome TEXT, idade NUMBER, sexo TEXT, curso TEXT, contato NUMBER)")  # Cria uma tabela única, para vevitar conflito com outra já criada.

cursor.execute(
    "INSERT INTO alunos VALUES('mja', 999, 'Masculino', 'dev-back-end', 9911111111 )")  # Insere dados na tabela.

banco.commit()  # Comenta o banco de dados

banco.close()  # Fecha o banco de dados
