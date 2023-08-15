"""
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par
ou é ímpar.
"""

num = int(input("Informe um número inteiro: "))

resposta = "este número é par" if num % 2 == 0 else "este número é ímpar"

print(f"{resposta}.")