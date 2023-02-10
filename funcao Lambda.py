def multiplicar_por(multiplicador):
    return lambda multiplicando: multiplicando * multiplicador

multiplicar_por_10 = multiplicar_por(10)
print(multiplicar_por_10(1))
print(multiplicar_por_10(2))
print(multiplicar_por_10(3))
print(multiplicar_por_10(4))
print(multiplicar_por_10(5))

multiplicar_por_5 = multiplicar_por(5)
print(multiplicar_por_5(1))
print(multiplicar_por_5(2))

