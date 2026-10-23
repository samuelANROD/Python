#argumentos
#posicionais
def apresentar(nome, idade):
    print(f"{nome} tem {idade} anos")

apresentar("sam", 19)

#nomeados
def apresentar02(nome = "sam", idade = 19):
    return f"{nome} tem {idade} anos"

print(apresentar02())

# ==================== 1. *args ====================
# *args junta todos os argumentos posicionais extras numa TUPLA

def somar(*args):
    print("args recebido:", args)     # mostra a tupla inteira
    total = 0
    for numero in args:               # args é uma tupla, então o for funciona
        total += numero
    return total

print(somar(1, 2, 3))                 # 3 argumentos
print(somar(10, 20, 30, 40))          # 4 argumentos, a mesma função serve
print(somar())                        # nenhum argumento: args vira ()

numeros = [5, 5, 5]
print(somar(*numeros))                # o * na chamada abre a lista em argumentos


# ==================== 2. **kwargs ====================
# **kwargs junta os argumentos NOMEADOS extras num DICIONÁRIO

def mostrar_perfil(**kwargs):
    print("kwargs recebido:", kwargs)
    for chave, valor in kwargs.items():   # .items() dá chave e valor juntos
        print(f"  {chave}: {valor}")

mostrar_perfil(nome="Sam", idade=19)
mostrar_perfil(nome="Ana", cidade="SP", curso="Python")


# ==================== 3. Tudo junto ====================
# Ordem na definição: normais, depois *args, depois **kwargs

def registrar_pedido(cliente, *itens, **detalhes):
    print(f"Cliente: {cliente}")      # cliente: parâmetro normal (obrigatório)

    print(f"Itens ({len(itens)}):")   # itens: tupla com os extras posicionais
    for item in itens:
        print(f"  - {item}")

    print("Detalhes:")                # detalhes: dicionário com os extras nomeados
    for chave, valor in detalhes.items():
        print(f"  {chave}: {valor}")

registrar_pedido("Sam", "pizza", "suco", "sorvete", entrega="rápida", pagamento="pix")
#                 |      \_____ vão para *itens ____/   \____ vão para **detalhes ____/
#                 └ vai para cliente