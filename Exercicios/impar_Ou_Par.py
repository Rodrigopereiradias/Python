def impar_ou_par():
    for numero1 in range(1, 21, 1):
        if numero1 % 2 == 0:
            print(f"{numero1} é par")
        else:
            print(f"{numero1} é impar")


def media_dos_pares():
    soma_pares = 0
    cont_pares = 0
    for numero2 in range(1, 21, 1):
        if numero2 % 2 == 0:
            soma_pares = soma_pares + numero2
            cont_pares += 1
        else:
            continue

    print(f'A media dos numeros pares é {soma_pares / cont_pares}')


impar_ou_par()
media_dos_pares()

