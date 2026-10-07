# A e B tem mesmos objetos A e C tem mesmos objetos e memórias
a = [1, 2, 3]
b = [1, 2, 3]
c = a

#mostrando a diferença de objetos e memoria
print(a == b) #comparação de objetos
print(a is b) #comparação de memória
print(a is c) #comparação de memória
print("")

#para ver memoria
print(id(a))
print(id(b))
print(id(c))
#compare a de A com a C