print('EMPRÉSTIMO')
print('Para solicitar seu empréstimo precisaremos de alguns dados para validar...')
nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))
salario = int(input('Quanto você recebe?'))
secret = int(input('senha secreta:'))

#flag = senha secreta, válida tudo independente da idade e sálario#

s = idade >= 18
n = salario >= 1700
flag = 1

print(s and n or flag == secret)
