def soma(*args):
    res = 0
    for item in args:
        res += item
    return res


def sub(*params):
    res = params[0]
    for i in params[1:]:
        res -= i


def mult(*params):
    res = 1
    for i in params:
        res *= i
    return res


def div(*params):
    res = params[0]
    for i in params[1:]:
        if i == 0:
            return -1
        res /= i


def calculadora(a, b, operador):
    if operador == '+':
        return a + b
    if operador == '-':
        return a - b
    if operador == '*':
        return a * b
    if operador == '/':
        return a / b

