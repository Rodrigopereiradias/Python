n = 5
media = 0
soma = 0
velho = 0
for m in range(1,n+1):
    print("---- {} Pessoa ----".format(m))
    id = int(input("Qual a idade: "))
    soma += id
    if id > velho :
        velho = id
media = soma / n
print('A media de idade é : {}'.format(media))
print('A pessoa mais velha tem : {} anos'.format(velho))