numeros = [(1, 2), (3, 4), (5, 6)]


def soma_de_tupla(pares):
    soma = []
    for nums in pares:
        sum = nums[0] + nums[1]
        soma.append(sum)
    return soma


print(soma_de_tupla(numeros))


