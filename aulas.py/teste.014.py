nome = input('Para prosseguir digite o seu nome: ')
print()
print(f'Olá {nome}, iremos calcular o preço a ser pago pela energia elétrica.')
print()

msg = '''
--------------------------
|ID    |Tipo de instalação
|I     |Indústrias    
|R     |Residências
|C     |Comércios
--------------------------
'''

print(msg)
tipo = input(f'{nome}, qual o id do tipo de instalação?')
qtd = float(input(f'{nome}, qual a quatidade de energia consumida em kWh?'))

if tipo == 'R':
    if qtd >= 500:
        valor = qtd * 0.4
    else:
        valor = qtd * 0.65
    print(f'{nome},o valor a ser pago é: {valor}')
elif tipo == 'C':
    if qtd >= 1000:
        valor = qtd * 0.55
    else:
        valor = qtd * 0.6
    print(f'{nome}, o valor a ser pago é: {valor}')
else:
    if qtd >= 5000:
        valor = qtd * 0.55
    else:
        valor = qtd * 0.6
    print(f'{nome} o valor a ser pago é: {valor}')
