#para registrar um valor a lista usando append()
a = []
while True:
    n = int(input('Digite um número:'))
    a.append(n)
    if n == 999:
        break
    print(a)
print('Acabou.')
