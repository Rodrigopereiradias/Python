lista = [1, 2, 3, 4, 5]

def triplica(item):
    return item * 1

nova_lista = map(triplica, lista)
print(list(nova_lista))