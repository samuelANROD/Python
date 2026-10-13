turma_1 = {'fulano_01', 'fulano_02', 'fulano_03'}
turma_2 = {'fulano_04', 'fulano_05', 'fulano_06', 'fulano_03'}

print(turma_1.intersection(turma_2)) #interseção ou seja o que tem em ambos os set
print(turma_1.union(turma_2)) #junção das duas
print(turma_1.difference(turma_2))
print(turma_1.symmetric_difference(turma_2))

#diferença normal pega os itens da 1 e fala qual nao tem na outra
#diferença simétrica fala os itens diferentes de ambas
