#a lógica é simples ele roda oq vc quiser ali a quantidade de vezes
for i in range(10):
    print(i, end=", ")

print(" ")
#for range podemos escolher qual valor iniciar
for j in range(1, 11):
    print(j, end= ", ")

#se vc quer usar o range para percorrer lista vc usa ele usando len
#pos len recebe o indice [0], [1]...
print(" ")
a = ['a', 'b', 'c']
for x in range(len(a)):
    print(a[x])