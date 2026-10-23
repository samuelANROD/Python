def fahrenheit_conversor(fahrenheit):
    return  (fahrenheit - 32) * 5 / 9

valor = int(input("digite temperatura: "))
resultado = fahrenheit_conversor(valor)
print(f" a temperatura {valor}F° em graus celsius é {resultado}")
