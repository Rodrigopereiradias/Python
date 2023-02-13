import datetime
def outAno():
    ano = int(input("Qual o ano vamos analizar?: "))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("o ano {} é Bissexto".format(ano))
    else:
        print("o ano {} não é Bissexto".format(ano))
def atualAno():
    ano = datetime.date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("o ano {} é Bissexto".format(ano))
    else:
        print("o ano {} não é Bissexto".format(ano))

def esco():
    escolha = str(input("Qual ano vamos analizar o atual ou outro: ").upper().strip())
    if escolha == "ATUAL":
        atualAno()

    elif escolha == "OUTRO":
        outAno()
    else:
        esco()
esco()