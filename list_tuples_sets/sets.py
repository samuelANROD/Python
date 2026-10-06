#principal diferença visível é a mudança de tuples() e lista[] para sets{}
set = {'a', 'b', 'c'}
set_2 = {'a', 'b', 'c', 'd'}
num = {1, 2, 3}
print(set)
print(num)

#use o print algumas vezes e ja fica claro a diferença
#sets não se importam com mudanças a ordem muda

#ele nao adiciona quando ja tem
set.add('a')
print(set)
print('a' in set) #ele verifica bem melhor que listas e tuples
print(" ")

#ele verifica em comun tambem
print(set.intersection(set_2))
#ele verifica a diferença
print(set.difference(set_2))
#unir
print(set.union(set_2))