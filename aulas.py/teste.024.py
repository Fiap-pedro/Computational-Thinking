#SOMA DOS NÚMEROS
#Jeito 1 (mais prático)
n = int(input('Digite um número:'))
i = 1
soma = 0
while n >= i:
    soma += i
    print(i, end='')
    if i != n:
        print('+', end='')
    i += 1
print(f'= {soma}')


#Jeito 2
'''n = int(input('Digite um número:'))
a = 1
soma = 0
while n > 0:
    soma += a
    a += 1
    n -= 1
    print(soma)'''

