"""
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2.
Deverá ser exibida na tela como resposta a média do aluno, e se ele está aprovado,
reprovado ou em prova final.Estas condições devem seguir as regras abaixo

abaixo de 3,0 = reprovado
entre = 3,0 e 6,9 = prova final
a partir de 7 aprovado
"""

nome = input("Informe o seu nome: ")
n1 = float(input("Informe a sua nota 1: "))
n2 = float(input("Informe a sua nota 2: "))

media = (n1 + n2) / 2

if (media < 3.0):
    print(f"Aluno {nome} você está reprovado, sua média é {media:.1f}.")
elif (media <= 6.9):
    print(f"Aluno {nome} você está de prova final, sua média é {media:.1f}.")
else:
    print(f"Aluno {nome} você está aprovado, sua média é {media:.1f}.")