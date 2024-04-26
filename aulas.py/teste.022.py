from time import sleep
n = int(input('Digite um número para ver sua tabuada: '))
a = 1
while a < 11:
    print(f'{n} x {a} = {n*a}')
    a += 1
    #sleep(0.5)
print('FIM.')
