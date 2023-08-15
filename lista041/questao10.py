"""
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o
segundo número informado é ou não um divisor do primeiro número informado.
"""

n1 = int(input("Informe um primeiro número: "))
n2 = int(input("Informe um segundo número: "))

resposta = "O segundo número é divisor do primeiro" if n1 % n2 == 0 else "O segundo número não é divisor do primeiro"

print(f"{resposta}.")