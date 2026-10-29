#iterators serve para vc percorrer list, dicionarios, tuplas, sets e etc
#só que ele percorre item por item
list = [1, 2, 3, 4]

my_list = iter(list)

print(next(my_list)) #ele imprime item 0
print(next(my_list)) #ele imprime item 1
print(next(my_list)) #ele imprime item 2
print(next(my_list)) #ele imprime item 3

#normalmente se usa loops for para percorrer assim:
print("")

for i in list:
    print(i)
