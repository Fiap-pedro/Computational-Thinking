pessoas = (("João", 17), ("Maria", 21), ("Pedro", 20), ("Ana", 18))

def maior_de_idade(pessoas):
    maiores = []
    for pessoa in pessoas:
            if pessoa[1] >= 18:
                maiores.append(pessoa)
    return tuple(maiores)


print(maior_de_idade(pessoas))
