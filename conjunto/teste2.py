a = [1, 2, 3, 8, 11]

b = [2, 6, 4, 7, 8]

valoresComuns = set(a) & set(b)

valoresSoDeA = set(a) - set(b)

valoresSoDeB = set(b) - set(a)

valoresNaoRepetidos = set(a) ^ set(b)


print(f'Valores comuns entr A e B: {valoresComuns}')
print(f'Valores só de A: {valoresSoDeA}')
print(f'Valores só de B: {valoresSoDeB}')
print(f'Valores não repetidos: {valoresNaoRepetidos}')
