n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor valor: '))
a = 0
while n1 <= n2:
    if n1 % 2 == 0:
        a += n1 #para incrementar um valor a cada vez que roda o código
    n1 += 1
print(a)

