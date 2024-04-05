'''a = 10
a,b = 3 * a, a
print(a, b)'''

'''a = 10
a = 3 * a
b = a
print(a,b)'''


#não recomendado
'''a = 10
b = 20
print(a,b)
a,b=b,a
print(a,b)'''

#recomendado
a = 10
b = 20
temp = 0

print(a, b)

temp = a
a = b
b = temp

print(a, b)

