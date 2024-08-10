n = int(input('LINHA: '))
estrelas = n * 2 - 1
count = 0
for i in range(n):
    print(f'{' '*(n-i-1)}{'*'*(2*i+1)}')


for i in range(n):
    print(f'{' ' * count}{'*' * estrelas}')
    estrelas -= 2
    count += 1


