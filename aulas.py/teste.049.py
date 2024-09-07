matriz = lambda linhas, colunas: [[int(input(f'Valor[{l}][{c}]:')) for c in range(colunas)] for l in range(linhas)]

print(matriz(3, 4))


