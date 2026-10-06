courses = ['historia', 'math', 'fisica', 'quimica']

#aqui vai mostrar todos os valores dessa lista simples
print(courses)

#aqui vai mostrar quantos valores ela armazena
print(len(courses))

#aqui para mostrar cada valor de uma forma especifica
print(courses[0], end= ' ')
print(courses[1], end= ' ')
print(courses[2], end= ' ')
print(courses[3])

#tem como voltar os valores exemplo
print(courses[-1]) #vc usa isso aqui basicamente quando quer acessar ultimo valor

#valores mais especificos
print(courses[0:2]) #vc especifica onde começa e onde termina
print(courses[0:])

#após daqui lembre-se qualquer alteração modifica toda a lista original

#como adicionar itens
courses.append('art') #comando nome da lista.append
print(courses)

#adicionar e falar posição
courses.insert(0, 'geografia')
print(courses)

#como adicionar varios itens na lista
courses_2 = ['gramatica', 'biologia', 'literatura']
courses.extend(courses_2)
print(courses)

#como remover itens
courses.remove('math')
courses.pop() #esse aqui sempre remove o ultimo termo
print(courses)

#como ver oq removeu usando pop
pop = courses.pop()
print(pop)

#reverter o que foi removido
courses.reverse()
print(courses)

#colocando em ordem alfabetica A-Z
courses.sort()
print(courses)

#classificar Z-A
courses.sort(reverse=True)
print(courses)

#como ordenar sem mudar lista original

sorted_courses = sorted(courses) #posso criar uma variavel assim fica mais facil
print(sorted_courses)
