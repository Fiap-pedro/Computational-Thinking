lista = [1, 3, 5, 7 ,9]


def soma(lista):
    if len(lista) == 1:
        return lista[0]

    return lista[0] + soma(lista[1:])


print(soma(lista))
