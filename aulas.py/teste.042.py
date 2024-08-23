qtd = 1000000
pi = 0
for i in range(qtd):
    termo = (-1)**i/(2*i+1)
    pi += 4*termo
    
print(pi)
