a = [12, 25, 37, 38, 41, 53, 65, 68, 71, 95]

valor = 53


def busca_binaria(a, valor):
    inicial = 0
    final = len(a) - 1
    while inicial <= final:
        meio = (final + inicial)//2
        if valor > a[meio]:
            inicial = meio + 1
        elif valor < a[meio]:
            final = meio - 1
        elif valor == a[meio]:
            return meio
    return -1


print(busca_binaria(a, valor))
