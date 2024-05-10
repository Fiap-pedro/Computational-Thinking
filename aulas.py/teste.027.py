#armazenando notas e mostrando a média
qtd = int(input('Quantas notas irá armazenar?'))
listaNotas = []
soma = 0
for c in range(1, qtd + 1):
    nota = float(input(f'{c}º nota:'))
    soma += nota
    listaNotas.append(nota)
media = soma / len(listaNotas)
print(f'As notas registradas: {listaNotas}')
print(f'A sua média foi: {media:.1f}')
