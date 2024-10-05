num = [90, 67, 30, 2, 54, 15, 7]

for tam in range(len(num) - 1, 0, -1):
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            maior = num[i]
            num[i] = num[i+1]
            num[i+1] = maior
    print(num)
