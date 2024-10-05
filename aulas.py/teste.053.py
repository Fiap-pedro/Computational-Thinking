lista = ["casa", "carro", "casa", "bicicleta", "carro", "carro", "bicicleta"]

def cria_dic(lista):
    dic = {}
    for palavra in lista:
        if palavra not in dic:
            dic[palavra] = 1
        else:
            dic[palavra] += 1
    return dic

print(cria_dic(lista))
