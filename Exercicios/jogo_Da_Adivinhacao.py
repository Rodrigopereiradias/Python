from random import randint
def inti () :
    print("   " * 20)
    print("Olá vamos jogar!")
    print("Qual a dificuldade?")
    print("Facil")
    print("Medio")
    print("Dificil")
    dif = input("qual a sua escolha? :").upper()
    print("   " * 20)

    if dif == "FACIL":
        facil()
    elif dif == "MEDIO":
        medio()
    elif dif == "DIFICIL":
        dificil()
def dnv() :
    print("..." * 20)
    print("..." * 20)
    print("Você quer tentar de novo?")
    print("..." * 20)
    res2 = input("sim ou não: ").upper()
    if  res2 == "SIM":
        inti()
    else:
        exit()
def facil ():
    comp = randint(0,5)
    print("Vou pensar em um numero de 0 a 5")
    print("tente adiinhar")
    print("   " * 20)
    res = int(input("qual a sua resposta "))
    print("   " * 20)
    if comp == res :
        print("eu pensei no {}".format(comp))
        print("parabens sua responsta esta correta")
        print("   " * 20)
        print("   " * 20)


    else:
        print("Eu pensei no numero {}".format(comp))
        print("Você erreou!!")
        print("   " * 20)
        print("   " * 20)
        dnv()
        print("   " * 20)

def medio ():
    comp = randint(0, 25)
    print("Vou pensar em um numero de 0 a 25")
    print("tente adiinhar")
    print("   " * 20)
    res = int(input("qual a sua resposta "))
    print("   " * 20)
    if comp == res:
        print("eu pensei no {}".format(comp))
        print("parabens sua responsta esta correta")
        print("   " * 20)
        print("   " * 20)
        dnv()


    else:
        print("Eu pensei no numero {}".format(comp))
        print("Você erreou!!")
        print("   " * 20)
        print("   " * 20)
        dnv()
def dificil ():
    comp = randint(0,100)
    print("Vou pensar em um numero de 0 a 100")
    print("tente adiinhar")
    print("   " * 20)
    res = int(input("qual a sua resposta "))
    print("   " * 20)
    if comp == res:
        print("eu pensei no {}".format(comp))
        print("parabens sua responsta esta correta")
        print("   " * 20)
        print("   " * 20)
        dnv()

    else:
        print("Eu pensei no numero {}".format(comp))
        print("Você erreou!!")
        print("   " * 20)
        print("   " * 20)
        dnv()



inti()