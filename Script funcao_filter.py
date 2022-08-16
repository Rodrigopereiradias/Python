lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def impar(item):
    return item % 2 != 0

def par(item):
    return item % 2 == 0

nova_lista2 = filter(par, lista)
nova_lista = filter(impar, lista)
print(list(nova_lista))
print(list(nova_lista2))