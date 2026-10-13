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

pequeno = {1, 2}
grande = {1, 2, 3, 4}
outro = {8, 9}

print(pequeno.issubset(grande))      # True: 1 e 2 estão em grande
print(grande.issubset(pequeno))      # False: 3 e 4 não estão em pequeno

print(grande.issuperset(pequeno))    # True: grande contém 1 e 2
print(pequeno.issuperset(grande))    # False

print(pequeno.isdisjoint(outro))     # True: nada em comum
print(pequeno.isdisjoint(grande))    # False: 1 e 2 são comuns