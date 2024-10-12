import requests

cep = input('CEP: ')
num = int(input('Número: '))

url = f'https://viacep.com.br/ws/{cep}/json/'

retorno = requests.get(url)
dados = retorno.json()

print(f'Rua: {dados['logradouro']}, {num}')
