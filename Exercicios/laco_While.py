from random import randint

v = 0
r = 0
nl = randint (1,10)
print("Vou pensar em um numero de 1 a 10. Tente adivinhar")
while r != nl:
    v += 1
    r = int(input("qual é o numero:"))
print("você tentou {} vezes ".format(v))
print("Parabens!!!!")
print("Você acertou o numero era {}".format(nl))