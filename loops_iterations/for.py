num = [1, 2, 3, 4, 5]

for i in num:
    print(i, end= "")
#ele basicamente da um print em cada um dos itens da lista usando "i"
#entao ele imprimi primeiro i = 1 depois i = 2...

#como usar break
print("")
for j in num:
    if j == 3:
        print("aqui esta o três")
        break
    print(j)

#como usar o continue
print("")
for x in num:
    if x == 3:
        print("aqui esta o três")
        continue
    print(x)

# principal diferença é que o break ele para quando a condição se realizar
# e o continue ele não para quando a condição se realiza