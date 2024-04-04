'''a = 2
b = 3
print(a>b)'''

#programa que avalia a nota e fala verdadeiro ou falso sobre a aprovação
n1 = int(input('sua nota no primeiro trimestre:'))
n2 = int(input('sua nota no segundo trimestre:'))
n3 = int(input('sua nota no terceiro trimestre:'))
media = n1 + n2 + n3 // 3
print(media>=7)
