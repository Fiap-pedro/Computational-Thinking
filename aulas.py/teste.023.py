#REFAZENDO O TESTE 20

msg = '''
|CÓDIGO      |PREÇO
| 1          |R$0,50
| 2          |R$1,00
| 3          |R$4,00
| 5          |R$7,00
| 9          |R$8,00
| 0          |SAI DO PROGRAMA
'''
print(msg)
resultado = 0
while True:
    comando = int(input('Qual o comando desejado? '))
    if comando == 0:
        print()
        break
    qtd = float(input('Qual a quantidade desejada? '))
    print()
    if comando == 1:
        resultado += qtd * 0.5
    elif comando == 2:
        resultado += qtd * 1
    elif comando == 3:
        resultado += qtd * 4
    elif comando == 5:
        resultado += qtd * 7
    elif comando == 9:
        resultado += qtd * 8
    else:
        print('Inválido.')
        print()
print('Você encerrou a compra, obrigado pela preferência.')
print(f'Preço total: R${resultado:.2f}')
