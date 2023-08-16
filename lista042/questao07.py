"""
Fazer um algoritmo que pergunte 2 números, e ao final,
exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais
"""

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))

if (n1 > n2):
    print(f"{n1} é maior que {n2}.")
elif ( n2 > n1):
    print(f"{n2} é maior que {n1}.")
else:
    print("Os dois números são iguais.")