"""
Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor
da diferença entre o maior valor e o menor valor lido
"""

n1 = int(input("Informe um valor inteiro: "))
n2 = int(input("Informe um segundo valor inteiro: "))

if (n1 > n2):
    print(f"O valor da diferença entre o maior e o menor número é {n1 - n2}.")
elif ( n2 > n1):
    print(f"O valor da diferença entre o maior número e o menor número é {n2 - n1}.")
else:
    print("O valor da diferença entre dois números iguais é 0.")