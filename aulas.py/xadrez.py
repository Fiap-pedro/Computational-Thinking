import matplotlib.pyplot as plt
linha = 8
coluna = 8

#List Comprehession
# xadrez = [[[255*((i+j) % 2), 255*((i+j) % 2), 255*((i+j) % 2)] for j in range(coluna)] for i in range(linha)]

matriz = []
cond = True
for j in range(linha):
    linha = []
    for i in range(coluna):
        cor = []
        for k in range(3):
            if cond:
                elemento = 255
            else:
                elemento = 0
            cor.append(elemento)
        cond = not cond
        linha.append(cor)
    cond = not cond
    matriz.append(linha)

print(matriz)
plt.imshow(matriz)
plt.axis('off')
plt.show()

