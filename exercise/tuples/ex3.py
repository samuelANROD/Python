#tente alterar e mostre uma mensagem de erro

teste = (1, 2, 3)

try:
    teste.append(4)
except AttributeError:
    print("não é possivel adicionar")