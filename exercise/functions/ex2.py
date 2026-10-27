def total_valor(produtos):
    total = 0

    for produto in produtos:
        total += produto["preço"]
    return total

produtos = [
    {"nome": "teclado", "preço": 150},
    {"nome": "mouse", "preço": 50},
    {"nome": "monitor", "preço": 800}
]

produtos.sort(key=lambda produto: produto["preço"], reverse=True)

print(produtos)
print(total_valor(produtos))
