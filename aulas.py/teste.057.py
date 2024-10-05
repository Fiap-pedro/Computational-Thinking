alunos = ["Ana", "Bruno", "Carlos", "Diana"]
notas = [85, 90, 78, 92]


def alunos_notas(alunos, notas):
    turma = {}
    for pessoas in range(len(alunos)):
        turma[alunos[pessoas]] = notas[pessoas]
    return turma


print(alunos_notas(alunos, notas))
