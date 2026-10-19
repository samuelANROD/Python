idade = int(input("digite sua idade: "))
carta = int(input("possui carta 0 para sim e 1 para não: "))

if idade >= 18 and carta == 0:
    print("pode dirigir")
elif idade >= 18 and carta ==1:
    print("faltou carta")
elif idade < 18 and carta ==0:
    print("não é possivel")
    print("carta só aos 18")
elif idade < 18 and carta==1:
    print("sem idade suficiente")
    print("sem carta")
else:
    print("digite valor positivo e 0 ou 1 para pergunta")