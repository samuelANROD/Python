#variável criada dentro da função. Ela só existe lá dentro e some quando a função termina.
def calcular():
    resultado = 10 * 2      # local
    print(resultado)

calcular()                  # 20

#variável criada fora de qualquer função. A função consegue ler ela.
nome = "Sam"                # global

def ola():
    print(f"Olá, {nome}")   # lê a global sem problema

ola()
#fato interresante aqui nas globais você pode criar variavel
#fora e uma dentro da função ambas com mesmo nome sem dar erro