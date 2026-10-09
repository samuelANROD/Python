num = []

for i in range(5):
    n = int(input(f"digite {i + 1} numeros: "))
    num.append(n)

num.sort()
print(f"em ordem crescente: {num}")

num.sort(reverse=True)
print(f"em ordem decrescente: {num}")