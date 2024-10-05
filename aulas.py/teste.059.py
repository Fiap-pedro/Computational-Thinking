palavras = ["banana", "maçã", "laranja", "uva", "abacaxi"]

def bubble_sort(palavras):
    for tam in range(len(palavras) - 1, 0, -1):
        for i in range(tam):
            if palavras[i] > palavras[i+1]:
                maior = palavras[i]
                palavras[i] = palavras[i+1]
                palavras[i+1] = maior
    return palavras


print(bubble_sort(palavras))
