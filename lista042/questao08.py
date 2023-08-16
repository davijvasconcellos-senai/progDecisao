"""
Fazer um algoritmo que pergunte 3 números, e ao final,
guarde na variável MAIOR o maior deste destes 3 números
inseridos.O valor da variável MAIOR deverá ser exibido.
"""

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe um outro número inteiro: "))
n3 = int(input("Informe um outro número inteiro: "))

maior = n1

if (maior < n2):
    maior = n2

if (maior < n3):
    maior = n3
print(f"O maior número entre estes 3 é {maior}.")