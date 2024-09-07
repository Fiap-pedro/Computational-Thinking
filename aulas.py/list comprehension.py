#Forma simples de criar listas

lista = [1 for i in range(10)]
print(lista)

lista2 = [i for i in range(10)]
print(lista2)

lista3 = [i*2 for i in range(10)]
print(lista3)

lista4 = [i for i in range(10) if i % 2 == 0]
print(lista4)


lista5 = [[i for i in range(10) if i%2 == 1] for i in range(3)]
print(lista5)
