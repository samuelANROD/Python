#ele vai rodar até que determinada condição seja realizada ou até aparecer um break
x = 1

while x <= 10: # ou seja ele vai executar até o "x" somado com 1 vire 10
    print(x, end=", ")
    x += 1

print("")
#isso fica mais desafiador com exercicios
#exemplo com break e while True
while True:
    if x > 10:
        break
    print(x, end=", ")
    x += 1
