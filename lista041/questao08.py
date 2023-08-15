"""
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
"""

num = int(input("Informe qualquer valor inteiro: "))

resposta = "Está na faixa de 1 a 10" if (num>=1) and (num<=10) else "Não está na faixa de 1 a 10"

print(f"{resposta}.")