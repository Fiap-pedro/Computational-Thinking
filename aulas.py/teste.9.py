dia = int(input('quantidade de dias:'))
hora = int(input('quantidade de horas:'))
minuto = int(input('quantidade de minutos:'))
segundo = int(input('quantidade de segundos:'))

n1 = dia*24*60*60 + hora*60*60 + minuto*60 + segundo

print(f'isso da {n1} em segundos')
