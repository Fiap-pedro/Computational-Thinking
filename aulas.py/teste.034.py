def fact(n):
    a = n - 1
    while a > 0:
        n *= a
        a -= 1
    return n

print(fact())
