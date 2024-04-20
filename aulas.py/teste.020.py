msg = '''
|CÓDIGO      |PREÇO
| 1          |R$0,50
| 2          |R$1,00
| 3          |R$4,00
| 5          |R$7,00
| 9          |R$8,00
'''
print(msg)
resultado = 0
while True:
    codigo = int(input('Escreva o código desejado: '))
    if codigo == 0:
        print(f'O preço total da compra é igual a R${resultado:.2f}')
        break
    qtd = int(input('Qual a quantidade desejada desse produto?'))
    if codigo == 1:
        resultado += 0.5 * qtd
    elif codigo == 2:
        resultado += 1 * qtd
    elif codigo == 3:
        resultado += 4 * qtd
    elif codigo == 5:
        resultado += 7 * qtd
    elif codigo == 9:
        resultado += 8 * qtd
    else:
        print('Código inválido, reinicie o programa.')


