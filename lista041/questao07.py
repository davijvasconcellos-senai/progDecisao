"""
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba
como resposta o módulo deste valor, ou seja, o número lido como sendo positivo.
"""

num = int(input("Informe um número inteiro positivo ou negativo: "))

modulo = (num, num * -1) [num < 0]

print(f"O módulo de {num} é {modulo}.")