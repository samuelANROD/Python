#modulo com função de par e impar e numeros primos
def func(n):
    if n % 2 ==0:
        print("par")
        return
    else:
        print("impar")
        return

def primo(n):
    if n <= 1:
        print("não primo")
        return

    for i in range(2, n):
        if n % i == 0:
            print("não primo")
            return

    print("primo")