def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 1000
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

pagamento = taximetro(3.5)
print(f'Valor:{pagamento} Reais')

