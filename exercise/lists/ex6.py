import math
xy = []

for i in range(3):
    x = int(input(f"digite x{i+1}: "))
    y = int(input(f"digite y{i+1}: "))

    xy.append((x, y))

distancia_1 = math.sqrt(
    (xy[1][0] - xy[0][0])**2 +
    (xy[1][1] - xy[0][1])**2
) #coordenadas 1 e 2
distancia_2 = math.sqrt(
    (xy[2][0] - xy[1][0])**2 +
    (xy[2][1] - xy[1][1])**2
) #coordendas 2 e 3

soma = distancia_1 + distancia_2

print(distancia_1)
print(distancia_2)
print(soma)