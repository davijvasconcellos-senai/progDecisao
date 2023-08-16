"""
Fazer um algoritmo que peça um número de 1 a 7, e ao final,
informe o dia da semana ( por extenso) correspondente ao número
inserido.Informar também a mensagem "número inválido" quando
o número inserido não corresponder à um dia da semana
"""

num = int(input("Informe um número de 1 a 7: "))

if ( num == 1):
    print(f"{num} é domingo.")
if ( num == 2):
    print(f"{num} é segunda-feira.")
if ( num == 3):
    print(f"{num} é terça-feira.")
if (num == 4):
    print(f"{num} é quarta-feira.")
if ( num == 5):
    print(f"{num} é quinta-feira.")
if ( num == 6):
    print(f"{num} é sexta-feira.")
if ( num == 7 ):
    print(f"{num} é sábado.")
else:
    print("Número inválido.")