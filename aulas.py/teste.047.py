A = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 1, 1],
    [1, 1, 1]
]


def esparsa(A):
    B = []
    for i in A:
        for j in i:
            B.append(j)
    if B.count(0) > len(B) / 2:
        return True
    else:
        return False


print(esparsa(A))
