velo = int(input('qual a velocidade do carro?'))

s = (velo - 80) * 5

if velo > 80:
    print(f'Você foi multado no valor de {s}, mais atenção da próxima!')

if velo <= 80:
    print('Parabens, voc esta nas normas de trânsito!')
