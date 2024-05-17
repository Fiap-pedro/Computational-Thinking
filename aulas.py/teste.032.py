def soma(n):
    cont = 0
    for i in range(1, n):
        if n % i == 0:
            cont += i
    return cont


def amigos(a, b):
    if soma(a) == b and soma(b) == a:
        return True
    else:
        return False


print(amigos(284, 220))
