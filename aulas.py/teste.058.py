saldos = {"Conta A": 1000, "Conta B": 1500}
movimentacoes = {"Conta A": -200, "Conta C": 500}


def contas_bancarias(saldos, movimentacoes):
    for key in movimentacoes:
        if key in saldos:
            saldos[key] += movimentacoes[key]
        else:
            saldos[key] = movimentacoes[key]
    return saldos


print(contas_bancarias(saldos, movimentacoes))
