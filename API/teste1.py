# para consultar as apis
import requests

cep = input('CEP: ')
n = input('Num: ')

#link do pacote json que consulta ceps
url = f'https://viacep.com.br/ws/{cep}/json/'

r = requests.get(url)

print(f'Rua: {r.json()["logradouro"]}, Número: {n}')

