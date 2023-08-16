"""
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2.
Deverá ser exibida na tela como resposta a média do aluno, e se ele está aprovado,
reprovado ou em prova final.Estas condições devem seguir as regras abaixo

abaixo de 3,0 = reprovado
entre = 3,0 e 6,9 = prova final
a partir de 7 aprovado
"""

n1 = float(input("Informe a sua nota 1: "))
n2 = float(input("Informe a sua nota 2: "))

media = (n1 + n2) / 2

if (media < 3):
    print(f"Você está reprovado, sua média é {media}.")

elif (media >= 3 and media == 6.9):
    print(f"Você está de prova final, sua média é {media}.")
else:
    print(f"Você está aprovado, sua média é {media}.")