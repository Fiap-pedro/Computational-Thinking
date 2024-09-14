matriz = lambda linhas, colunas: [[int(input(f'valor[{i}][{j}]:')) for j in range(colunas)] for i in range(linhas)]


print(matriz(3, 4))
