#basicamnete uma função dentro de outra função
#pode-se dizer que é o tipo mais dificil de função
def so_positivos(func):
    def wrapper(*args):
        for numero in args:
            if numero <= 0:
                print("Erro: só aceito números positivos")
                return None              # não chama a função original
        return func(*args)               # tudo certo: roda a original
    return wrapper

@so_positivos
def multiplicar(a, b):
    return a * b

print(multiplicar(3, 4))     # 12
print(multiplicar(-3, 4))    # Erro: só aceito números positivos / None