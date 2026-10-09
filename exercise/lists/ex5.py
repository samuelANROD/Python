num = [1, 2, 3, 4, 5]

n = int(input("digite qual numero deseja rotacionar: "))

for i in range(n):
    ultimo = num[-1]
    for j in range(len(num) - 1, 0, -1): #len - 1 = 4, 0 é o limite e -1 é andar para tras
        num[j] = num[j - 1]

    num[0] = ultimo

print(num)
