def cria_matriz(qtdLinhas, qtdColunas):
    matriz = []
    for i in range(qtdLinhas):
        linha = []
        for c in range(qtdColunas):
            linha.append(int(input(':')))
        matriz.append(linha)
    return matriz


def printa(matriz):
    for i in range(len(matriz)):
        print(f'A{i}- ', end='')
        for n in range(len(matriz)):
            print(matriz[i][n], end=' ')
        print()


printa(cria_matriz(3, 3))

