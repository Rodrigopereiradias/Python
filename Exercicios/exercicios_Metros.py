import math
def calmetros ():
    try:
        medida = float(input('uma disntacia em metros: '))
        cm = medida * 100
        mm = medida * 1000
    except:
        print('Ops, houve um problema')
        calmetros()
    else:
        print('resultado {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
        init()
def calsoma ():
    try:
        n1 = int(input('Digite um numero:  '))
        n2 = int(input('Digite um numero:  '))
        res = n1 + n2
    except:
        print('Ops, houve um problema')
        calsoma()
    else:
        print('O resultado da soma é : {}'.format(res))
        init()
def calsubi ():
    try:
        n1 = int(input('Digite um numero:  '))
        n2 = int(input('Digite um numero:  '))
        res = n1 - n2
    except:
        print('Ops, houve um problema')
        calsubi()
    else:
        print('O resultado da subitração é : {}'.format(res))
        init()
def calmuti():
    try:
        n1 = int(input('Digite um numero:  '))
        n2 = int(input('Digite um numero:  '))
        res = n1 * n2
    except:
        print('Ops, houve um problema')
        calmuti()
    else:
        print('O resultado da mutiplicação é : {}'.format(res))
        init()
def caldivi ():
    try:
        n1 = float(input('Digite um numero:  '))
        n2 = float(input('Digite um numero:  '))
        res = n1 / n2
    except:
        print('Ops, houve um problema')
        caldivi()
    else:
        print('O resultado divisão é : {}'.format(res))
        print('O resultado simplificado : {:.0f}'.format(res))
        init()
def calraiz ():
    try:
        n1 = float(input('Digite um numero:  '))
        raiz = math.sqrt(n1)
    except:
        print('Ops, houve um problema')
        caldivi()
    else:
        print('A raiz de {}  é : {}'.format(n1, math.floor(raiz)))
        init()


def init () :
    print('Calculadora')

    print('soma')
    print('divisão')
    print('mutiplicação')
    print('subitração')
    print('raiz')
    print('metros')
    print('sair')
    operacao = input('Qual a operação que vc vai utilizar: ')
    if operacao == 'soma':
        calsoma()
    elif operacao == 'subitração':
        calsubi()
    elif operacao == 'mutiplicação':
        calmuti()
    elif operacao == 'divisão':
        caldivi()
    elif operacao == 'metros':
        calmetros()
    elif operacao == 'raiz':
        calraiz()
    elif operacao == 'sair':
        print('Obrigado e volte sempre!!')
    else:
        print('Ops, houve um problema')
        init()
init()
