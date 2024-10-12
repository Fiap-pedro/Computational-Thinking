# a = [10, 12, 41, 68, 95, 21]
a = [12, 68, 95, 41, 10, 71]

for i in range(len(a)):
    aux = a[i] # aux = 21
    j = i-1
    while j >= 0 and a[j] > aux:
        a[j+1] = a[j]
        j -= 1

    a[j+1] = aux
    print(a)





