def fatorial(n):
    if n == 0:
        return 1
    else:
        aux = fatorial(n-1)
        return n * aux
