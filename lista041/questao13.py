"""
Desenvolver um programa que pergunte 3 valores (variáveis a,b e c)  e ao final apresente-os
e ao final apresente-os em ordem crescente
"""

a = int(input("Informe o 1° número inteiro: "))
b = int(input("Informe o 2° número inteiro: "))
c = int(input("Informe o 3° número inteiro: "))

if (a > b):
    aux = a
    a = b
    b = aux
if (a > c):
    aux = c
    a = c
    c = aux

if (b > c):
    aux = b
    b = c
    c = aux

print(f"Os valores em ordem crescente são {a},{b} e {c}.")