# para criar uma recursão, tem que achar o caso base da função (0! = 1 ==> if n == 0: return 1) logo em seguida coloca a formula desejada usando a formula para que ela se repita
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


print(fatorial(5))
