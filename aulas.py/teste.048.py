def f2(a):
    global c
    c = 10
    return a+x+c


x = 4
print(f2(3))
print(c)
