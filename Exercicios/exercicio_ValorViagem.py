km = float(input("Sua viagem terá quantos quilometors percorridos?: "))
if km >= 200:
    valor = km * 0.45
    print('A sua passagem custa {} Reais'.format(valor))
else:
    valor = km * 0.35
    print('A sua passagem custa {} Reais'.format(valor))

