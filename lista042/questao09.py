"""
Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final,
informe na tela se a pessoa é menor de idade, maior de idade ou
 se é maior de 65 anos de idade
"""

idade = int(input("Informe a sua idade: "))

if (idade <= 17):
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")
if (idade > 65):
    print("você tem mais de 65 anos de idade.")