num = [1,6,2,5,4,9,2,0]
#achar onde esta exatamente a posição de cada valor
print(num)
print(num.index(2), end= ', ')
print(num.index(9), end= ', ')
print(num.index(0),)
print(" ")

#checar se tem tal valor na lista
print(7 in num)
print(2 in num)
print(" ")

#demonstrando sort com valores numéricos
num.sort()
print(num)
print(" ")

#amior para menor
num.sort(reverse=True)
print(num)
print(" ")

#ordenando sem mudar ordem original
sorted_num = sorted(num) #utilize isso aqui
print(sorted_num)
print(" ")

#min max e sum
print(min(num), end= ", ") #minimo
print(max(num), end=", ") #maximo
print(sum(num)) #soma valores
print(" ")
