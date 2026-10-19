n = []
for i in range(3):

    num = int(input("digite tres valores: "))
    n.append(num)
    print(n)

if n[0] > n[1] and n[0] > n[2]:
    print(f"o maior é o: {n[0]}")

elif n[1] > n[0] and n[1] > n[2]:
    print(f"o maior é: {n[1]}")

else:
    print(f"o maior é: {n[2]}")