n1 = int(input('digite um número:'))

if n1 % 2 == 0:
    if n1 < 100:
        print(f'{n1} é par e menor que cem')

if n1 % 2 == 0:
    if n1 > 100:
        print(f'{n1} é par e maior que cem')

if n1 % 2 != 0:
    if n1 < 100:
        print(f'{n1} é ímpar e menor que cem')

if n1 % 2 != 0:
    if n1 > 100:
        print(f'{n1} é ímpar e maior que 100')

elif n1 == 100:
    print(f'{n1} é par e igual á 100')
print('__FÉ__')
