
class CadastroAlunos:
    def __init__(self):
        self.quantidade = 0

    def cadastrar_aluno(self, nome, idade, **informacoes):
        aluno = {
            "nome": nome,
            "idade": idade
        }

        aluno.update(informacoes)
        self.quantidade += 1

        return aluno

    def calcular_notas(self, *notas):
        if len(notas) == 0:
            return "Nenhuma nota informada"

        media = sum(notas) / len(notas)
        maior = max(notas)
        menor = min(notas)

        return {
            "media": media,
            "maior nota": maior,
            "menor nota": menor
        }


cadastro = CadastroAlunos()

aluno1 = cadastro.cadastrar_aluno(
    "Samuel",
    19,
    curso="Engenharia de Software",
    cidade="São Paulo",
    email="samuel@email.com"
)

aluno2 = cadastro.cadastrar_aluno(
    "Carlos",
    21,
    curso="Sistemas de Informação"
)

print("Ficha do aluno:", aluno1)
print("Ficha do aluno:", aluno2)

print("Notas:", cadastro.calcular_notas(8, 7, 9, 10))

print("Alunos cadastrados:", cadastro.quantidade)
