#Para salvar mais de um item em uma lista
'''animais = []
print(animais)
while True:
    a = input('Nome:')
    if a == '0':
        print('fim')
        break
    b = int(input('Idade:'))
    animais.append(a)
    animais.append(b)
    print(animais)'''

#Para copiar uma lista antes de ser alterada
'''a = [1, 2, 3, 4, 5]
b = a[:]

a[0] = 0

print((a))
print(b)'''

#Para remover um item de uma lista
'''a = [1, 2, 3, 4, 5]
a.pop(2)
print(a)'''

#
'''a = [1, 2, 3, 4, 5]
for i in a:
    print(i)'''

#
'''from time import sleep
for i in range(10, 0, -1):
    print(i)
    sleep(0.4)
#print('FELIZ ANO NOVO!')

n = 0
while n > -11:
    print(n)
    sleep(0.4)
    n -= 1
print('FIM')'''

'''a = []
nota = 1
while nota != 0:
    nota = int(input('Digite sua nota: '))
    a.append(nota)
    print(a)'''
