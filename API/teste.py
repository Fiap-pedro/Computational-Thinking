import requests

url = f'pegar_url/{complemento}'

r = requests.get(url)

print(r)
print(r.text)
print(r.json())
