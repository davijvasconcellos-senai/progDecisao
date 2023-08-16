"""
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa
e o ano atual.Ao final o algoritmo deverá exibir na tela a idade
da pessoa.Porém, se o usuário inserir o ano de nascimento com
valor maior que o ano atual, o cálculo de idade não deverá
ser feito, e então deverá surgir a seguinte mensagem na tela:
"Dados inseridos estão incorretos"
"""

nascimento = int(input("Informe o ano do seu nascimento: "))
ano_atual = int(input("Informe o ano atual: "))

idade = ano_atual - nascimento

if ( ano_atual > nascimento):
    print(f"Você possui {idade} anos de idade.")
else:
    if (ano_atual < nascimento):
        print("Dados inseridos estão incorretos.")