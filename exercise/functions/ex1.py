def validar_senhas(senha):
    erros = []
    if len(senha) < 8:
        erros.append("erro menos de 8 caracteres")
    if not any(caractere.isdigit() for caractere in senha):
        erros.append("não possui numeros")
    if not any(caractere.isupper() for caractere in senha):
        erros.append("não possui letra maiuscula")

    if len(erros) == 0:
        return "senha aceita"
    else:
        return "senha recusada " + ", ".join(erros)

senhas = [
    "Abc12342",
    "abc1234",
    "BBc109283",
    "aB1",
    "Senha123"
]

for i in senhas:
    print(i, "->", validar_senhas(i))