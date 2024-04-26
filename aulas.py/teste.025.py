#FIBONACCI

n = int(input('Até que termo você quer da sequência de Fibonacci? '))

t1 = 0
t2 = 1
i = 1

print(t1)
print(t2)
while i <= n - 2:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3)
    i += 1
