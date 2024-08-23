v = []
w = []
z = []

qtd = 1000000

for i in range(qtd):
    v.append(1)

for i in range(qtd):
    w.append((-1)**i)

for i in range(qtd):
    z.append(2*i+1)


def produtoInterno(lista1, lista2, lista3):
    soma = 0
    if len(v) == len(w):
        for i in range(len(v)):
            termo = v[i] * w[i] / z[i]
            soma += termo
        return soma
    else:
        return 'none'


print(4 * produtoInterno(v, w, z))
