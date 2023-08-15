"""
Desenvolver um programa que pergunte um número.Se este número for maior que 20, então ele deverá exibir a metade
deste número, senão, ele deverá exibir o número sem exibições
"""

num = float(input("Informe um número (inteiro): "))

if (num > 20):
    print(f"A metade de {num} é {num/2}.")
else:
    print(f"{num}.")