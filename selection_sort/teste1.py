select = [68, 95, 41, 12, 64, 71]


def i_v_menores(index, lista):
    menor = select[index]
    indice = index
    for i in range(index+1, len(select)):
        if menor > select[i]:
            menor = select[i]
            indice = i
    return indice, menor


def selection_sort(lista):
    for i in range(len(lista) - 1):
        aux = i_v_menores(i, lista)[1]
        lista[i_v_menores(i, lista)[0]] = lista[i]
        lista[i] = aux
    return lista


print(selection_sort(select))

