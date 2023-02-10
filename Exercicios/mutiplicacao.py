valor = 20

def multiplica(fator):
    global valor
    valor = valor * fator
    print("Resultado", valor)
multiplica(3)
multiplica(3)


valor = 20

def multiplica(valor, fator):
    valor = valor * fator
    return valor

print("Resultado", multiplica(valor, 3))
print("Resultado", multiplica(valor, 3))

valores = [10, 20, 30]

def altera_lista(lista):
    lista[2] = lista[2] + 10
    return lista

print("Nova lista", altera_lista(valores))
print("Nova lista", altera_lista(valores))


valores = [10, 20, 30]

def altera_lista(lista):
    nova_lista = list(lista)
    nova_lista[2] = nova_lista[2] + 10
    return nova_lista

print("Nova lista", altera_lista(valores))
print("Nova lista", altera_lista(valores))