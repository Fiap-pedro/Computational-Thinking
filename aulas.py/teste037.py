def y(x):
    if x <= 2:
        return x
    elif x <= 3.5:
        return 2
    elif x < 5:
        return 3
    else:
        return x**2 - 10*x + 28


print(y(3))
