#pi

def pi(loop):
    x = 0
    n = 0
    for c in range(0, loop):
        x += 2 * (3**(1/2)) * ((-1)**n) / (3**n * (2*n+1))
        n += 1
    return x

print(pi(33))

