"""
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba
mensagem informando que o aluno foi aprovado se a média escolar for maior
ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando
essa condição. Apresentar junto com a mensagem de aprovação ou reprovação
o valor da média obtida pelo aluno.
"""

n1 = float(input("Informe a sua 1° nota: "))
n2 = float(input("Informe a sua 2° nota: "))
n3 = float(input("Informe a sua 3° nota: "))
n4 = float(input("Informe a sua 4° nota: "))

media = (n1 + n2 + n3 + n4) / 4

if ( media >= 5):
    print(f"Sua média é {media},você está aprovado.")
else:
    print(f"Sua média é {media}, você está reprovado.")