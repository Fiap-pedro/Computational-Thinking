numeros = [71, 10, 19, 57, 23, 42, 12, 17, 29]

for vezes in range(len(numeros)-1, 0, -1):
    for i in range(len(numeros)-1):
        if numeros[i] < numeros[i+1]:
            menor = numeros[i]
            numeros[i] = numeros[i+1]
            numeros[i+1] = menor
        print(numeros)
