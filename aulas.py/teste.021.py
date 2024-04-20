a = 0
while True:
    senha1 = int(input('Digite a senha: '))
    senha2 = int(input('Digite a senha novamente: '))
    if senha1 == senha2:
        print('Acesso permitido.')
        break
    else:
        a += 1
        print('Acesso negado, tente novamente.')
        if a == 3:
            print('Bloqueado!')
            break

