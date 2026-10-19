while True:

    dia = int(input("digite um valor de 1 a 7 ou 0 para encerrar: "))

    if dia == 1:
        print("segunda")
    elif dia == 2:
        print("terça")
    elif dia == 3:
        print("quarta")
    elif dia == 4:
        print("quinta")
    elif dia == 5:
        print("sexta")
    elif dia == 6:
        print("sabado")
    elif dia == 7:
        print("domingo")
    elif dia == 0:
        print("fim")
        break
    else:
        print("digite valor de 1 a 7")