velo = int(input("Qual era a velocidade do carro?: "))
if velo > 80:
    multa = velo - 80
    valor = multa *7
    print('A sua velociade é {}, a sua multa será de R$: {}.00'.format(velo, valor))
else:
    print(' boa viagem')