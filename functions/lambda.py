#é: uma função pequena, de uma linha só, sem nome. Ela tem a forma lambda parâmetros: expressão
nomes = ["Ana", "Bartolomeu", "Li"]
print(sorted(nomes, key=lambda n: len(n)))   # ['Li', 'Ana', 'Bartolomeu']

nums = [1, 2, 3, 4]
print(list(filter(lambda n: n % 2 == 0, nums)))   # [2, 4]
print(list(map(lambda n: n ** 2, nums)))          # [1, 4, 9, 16]