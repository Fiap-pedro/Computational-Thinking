velo = int(input('qual a velocidade do carro?'))

if velo > 80:
    s = (velo - 80) * 5
    print(f'Você foi multado no valor de {s}, mais atenção da próxima!')

if velo <= 80:
    print('Parabens, voc esta nas normas de trânsito!')
