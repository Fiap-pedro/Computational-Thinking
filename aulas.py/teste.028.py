#fila
from time import sleep
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for c in range(11, 52):
    print(a)
    a.pop(0)
    a.append(c)
    sleep(0.5)

