
from random import randint
def reload():
    cont = randint(0, 100)
    cont2= cont
    val = cont
    print("{}".format(val))
    for r in range(0,cont2) :
        cont =  randint(0,100)
        val -= 1
        print("{}".format(val))

reload()