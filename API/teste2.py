import requests

def poke(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    r = requests.get(url)
    var = r.json()
    return var['id'], var['types'][0]['type']['name']


pokemon = 'pikachu'
tipo = poke(pokemon)[1]
id = poke(pokemon)[0]

print(f'O id do {pokemon} é {id}.')
print(f'{pokemon} é do tipo {tipo}!')
