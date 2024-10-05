a = [12, 68, 95, 41, 25, 71]
print(a)

for tam in range(len(a)-1, 0, -1):
    for i in range(tam):
        if a[i] > a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
        print(a)

