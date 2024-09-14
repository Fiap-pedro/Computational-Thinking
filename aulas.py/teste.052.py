dados = [
    {"dia": 21, "mes": 2, "ano": 2019, "temp": 30.5},
    {"dia": 18, "mes": 3, "ano": 2019, "temp": 29.1},
    {"dia": 22, "mes": 4, "ano": 2019, "temp": 28.5},
    {"dia": 17, "mes": 5, "ano": 2019, "temp": 26.4}
]

for c in dados:
    print(f'{c["dia"]}/0{c["mes"]}/{c["ano"]}: Temperatura: {c["temp"]}')
