import _sqlite3
import pandas as pd

conexao = _sqlite3.connect("produtos.db")

cursor = conexao.cursor()
cursor.execute("SELECT * FROM produtos")

resultado = cursor.fetchone()
print(resultado)

cursor.close()
conexao.close()
