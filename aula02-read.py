import sqlite3

banco = sqlite3.connect("banco-escolar.db")

cursor = banco.cursor()


# cursor.execute("SELECT * FROM alunos")#Selecionando/Buscando todos dados da tabela
# Buscando uma informação específica/exata.
cursor.execute("SELECT * FROM alunos WHERE curso = 'engenharia' ")

alunos = cursor.fetchall()  # função para percorrer a tabela (as tuplas)

print(alunos)

# print(alunos[0])#para um índice
