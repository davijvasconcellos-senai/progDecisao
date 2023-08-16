"""
Fazer um algoritmo que pergunte a sigla de um estado brasileiro
(UF-> Undidade Federativa), e ao final, informe na tela se o
estado inserido está ou não na Região Sudeste
"""

uf = ("Informe a sigla de um estado brasileiro: ")

if (uf == "ES"):
    print("Espírito Santo faz parte da Região Sudeste.")
if (uf == "MG"):
    print("Minas Gerais faz parte da Região Sudeste.")
if (uf == "RJ"):
    print("Rio de Janeiro está na Região Sudeste.")
if (uf == "SP"):
    print("São Paulo está na Região Sudeste.")
else:
    print("Este estado não faz parte da Região Sudeste.")