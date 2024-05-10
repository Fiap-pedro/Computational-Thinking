#02d ==> para que os números que não tiver duas casas ser completada com 0
from time import sleep
hora = 24
minuto = 60
segundo = 60
print(f'{hora}:{minuto}:{segundo}')
while True:
    hora -= 1
    print(f'{hora}:{minuto}:{segundo}')
    if hora == 0:
        print()
        minuto -= 1
        if minuto == 0:
            segundo -= 1






