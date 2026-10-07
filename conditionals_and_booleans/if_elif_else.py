# atribuir: =
#igualdade: ==
#não igual: !=
#menor: <
#maior: >
#maior igual: >=
#menor igual: <=

print("opcões possiveis: Python e Java")
language = input("digite sua linguagem favorita de programação: ")

if language == 'Python': #primeira verificação
    print("sua linguagem favorita é Python")
elif language == 'Java': #segunda verificação usa elif
    print("sua linguagem favorita é Java")
else: #opção caso pessoa digite algo fora do esperado
    print("escolha Python ou Java")

print("-" * 25)
#and só roda se as duas forem verdadeiras
#or roda se uma das duas forem verdadeiras
#not ele inverte valor booleano

user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('admin page')
else:
    print('sem credenciais')

#exemplo not

name = True
#ele inverte os valores booleanos
if not name:
    print('digite seu nome: ')
    name = input()
else:
    print("bem vindo")




