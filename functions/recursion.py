#função que resolve um problema
#exemplo 01:
def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

num = int(input("digite valor: "))
resultado = fatorial(num)
print(resultado)