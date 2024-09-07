# Questão 1
def f(x):
    if x < -2:
        y = x**2 + 3*x - 4
    elif x < 0:
        y = 2*x + 5
    elif x < 4:
        y = x**(1/2)
    elif x < 6:
        y = x**3 - 3*x**2 - 10*x
    elif x < 8:
        y = 3*x**2 - 4*x - 20
    else:
        y = 10
    return y


#Questão 2
def le_matriz(l, c):
    matriz = []
    for j in range(l):
        linha = []
        for i in range(c):
            linha.append(int(input(f'[{j}][{i}]:')))
        matriz.append(linha)
    return matriz


#Questão 3
def tamanho(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    return [linhas, colunas]


#Questão 4
def subtracao(a, b):

    if len(a) == len(b) and len(a[0]) == len(b[0]):
        c = []
        for j in range(len(a)):
            linha = []
            for i in range(len(a[0])):
                linha.append(a[0][i] - b[0][i])
            c.append(linha)

        return c


#Questão 5
A = [
    [1, 2, 3],
    [5, 8, 10]
]
def transposta(A):
    B = []
    for j in range(len(A[0])):
        linha = []
        for i in range(len(A)):
            linha.append(A[i][j])
        B.append(linha)
    return B

print(transposta(A))


