"""
Desenvolver um programa que pergunte e exiba a informação de que ele é positivo, negativo ou nulo
"""

num = int(input("Informe um número inteiro qualquer: "))

if (num > 0):
    print(f"{num} é positivo.")
elif ( num < 0):
    print(f"{num} é negativo.")
else:
    print(f"{num} é nulo.")