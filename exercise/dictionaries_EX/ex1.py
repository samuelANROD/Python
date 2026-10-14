dados = {'name': 'sam', 'age': 19, 'city': 'new york'}

for keys, value in dados.items():
    print(keys, ": ", value)

#removendo e adicionando

dados.update({'age': 20})
del dados['city']
dados['work'] = 'aeropace'

for i, j in dados.items():
    print(i, ": ", j)
