repetidos = [1, 1, 2, 3]
sem_repetidos = []

for i in repetidos:
    if i not in sem_repetidos:
        sem_repetidos.append(i)

print(sem_repetidos)
