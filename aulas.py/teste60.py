lista = [1, 4, 6, 5]

def busca(lista,item):
    for i, j in enumerate(lista):
        if lista[i] == item:
            return i
    return -1


print(busca(lista, 5))
