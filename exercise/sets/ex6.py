alfabeto = set("abcdefghijklmnopqrstuvwxyz")
frase = "Um pequeno jabuti xereta viu dez cegonhas felizes"
letras = set(frase.lower())

print(alfabeto.issubset(letras))   # True = é pangrama
print(alfabeto - letras)           # letras que faltam