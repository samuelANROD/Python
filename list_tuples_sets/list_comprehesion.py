frutas = ["banana", "maça", "pera", "abacaxi", "kiwi"]
new_frutas = []

for i in frutas:
    if "a" in i:
        new_frutas.append(i)

print(new_frutas)
#percebe-se que se trata de criar nova lista com uma caracterista da lista original

#essa é outra maneira de escrever uma compressão de lista
letras = ["a", "b", "c"]
letras_02 = [j for j in letras if "b" in j]

print(letras_02)