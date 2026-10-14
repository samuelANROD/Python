palavra = 'banana'
contagem = {}

#esta meio que criando para cada letra uma chave
for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1
#demosntração
print(contagem.keys())
print(contagem.values())
print(contagem.items())
