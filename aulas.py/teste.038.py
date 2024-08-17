from teste import *

valores = []
qtde = int(input('Digite a quantidade de números que deseja somar: '))
for i in range(0, qtde):
    valores.append(float(input('Digite o valor: ')))

print(soma(*valores))
