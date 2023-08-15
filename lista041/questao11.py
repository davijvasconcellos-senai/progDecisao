"""
Desenvolver um programa que pergunte um número inteiro de 3 alagarismos e apresente como
resultado somente o algarismo das centenas
"""

num = int(input("informe um número inteiro com 3 alagarismo: "))

if (num >= 100) and (num <= 999):
    print(f"{num} possui 3 algarismos.")

    centena = num // 100
    print(f"O algarismo das centenas é {centena}.")