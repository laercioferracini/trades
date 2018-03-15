#arquivo para exibir as ranges de lucro na compra e venda de criptomoedas

def rangeLucro():
    """
    Fórmulas
        Cálculo da comissão (feeBittrex * valorTotal)
        Cálculo do alvo ((precoOrdem * alvo)/100)
        Cálculo do lucro (alvo * precoOrdem * volumeOrdem)
        Cálculo da comissão de venda( feeBittrex * (valorTotal + lucro))
    """

    # variaveis
    saldoBTC = 0.01293111

    feeBittrex = 0.25
    valorTotal = 0.00150000
    precoOrdem = 0.00000100

    comissao = (feeBittrex * valorTotal) / 100
    volumeOrdem = (valorTotal - comissao) / precoOrdem
    precoVendido = 0
    lucro = 0
    satoshis = 0

    listaAlvosPositivos = None
    listaAlvosNegativos = None

    # format(,'.8f')
    print('Tabela alvos de venda {}!'.format("moedas virtuais"))
    # print(valorTotal - comissao, format(precoOrdem, '.8f'), format(comissao, '.8f'), format(volumeOrdem, '.8f'))
    print(repr('Alvos %').rjust(1), repr('Satoshis').rjust(12), repr('Preço Vendido').rjust(16),
          repr('Lucro').rjust(10),
          repr('Fee Venda').rjust(16), repr('Total BTC').rjust(16))

    for alvo in range(1, 10):
        satoshis = (precoOrdem * alvo) / 100
        lucro = satoshis * volumeOrdem
        precoVendido = precoOrdem + satoshis
        comissao = (feeBittrex * (valorTotal + lucro)) / 100
        valorTotalBTC = valorTotal + lucro
        # print(repr(alvo).rjust(7), repr(format(satoshis, '.8f')).rjust(16), repr(format(precoVendido, '.8f')).rjust(16))

        listaAlvosPositivos = listaAlvosPositivos, alvo, format(satoshis, '.8f'), format(precoVendido, '.8f'), \
                              format(lucro, '.8f'), format(comissao, '.8f'), format(valorTotalBTC, '.8f'),

    # print(listaAlvosPositivos)
    return listaAlvosPositivos


# for alvo in range(-10, -1):
#     satoshis = (precoMoedaEmBTC * alvo)/100
#     precoVendido = precoMoedaEmBTC + satoshis
#     print(repr(alvo + '%').rjust(7), repr(format(satoshis, '.8f')).rjust(15), repr(format(precoVendido, '.8f')).rjust(16))

