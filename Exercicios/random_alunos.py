import random
al1 = input("Primeiro aluno ")
al2 = input("Segundo aluno ")
al3 = input("Terceiro aluno ")
al4 = input("Quarto  aluno ")
al5 = input("Quinto aluno ")

list = [ al1, al2, al3, al4, al5]

escolhido =random.choice(list)

print('O escolhido é {}'.format(escolhido))