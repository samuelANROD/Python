#criar tuple de 1 até 10 imprimir terceiro e setimo depois só os pares

num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(num[2]) #terceiro
print(num[6]) #sétimo

#aqui para imprimir valores pares
for i in num:
    if i % 2 ==0:
        print(num)
