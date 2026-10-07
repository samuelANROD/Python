#dicionario ele funciona com chave-valor
#veja os exemplos:
students = {'name': 'john', 'age': 25} #cada um armazena seu valor(dados)

#adicionando informação
students['last_name'] = 'Rodrigues'

print(students) #print normal
print(len(students)) #quantidades de itens dentro
print(students.keys()) #só as chaves
print(students.values()) #só os valores(dados)
print(students.items()) #mostra os pares chave-valor

#tambem é possivel chamar especifico
print(students['name'])

#pode procurar dentro dela
print(students.get('age'))
print(students.get('phone')) #none exemplo
print(students.get('phone', 'Not Found')) #atribuindo mensagem

#como atualizar(mudar varios ao mesmo tempo)
students.update({'name': 'sam', 'age': 19})
print(students)

#deletando itens
del students['age']
print(students)
#removendo com pop metodo
# age = students.pop('age')
# print(age)