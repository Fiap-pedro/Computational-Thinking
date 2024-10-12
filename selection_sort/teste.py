select = [68, 95, 41, 102, 64, 71]

def indice_valor_menores(lista):
    index = menor = select[0]
    for i, v in enumerate(select):
        if menor > v:
            menor = v
            index = i
    return index, menor


print(f'Índice: {indice_valor_menores(select)[0]} Valor: {indice_valor_menores(select)[1]}')
