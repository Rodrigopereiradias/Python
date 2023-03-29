"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

'''
print('Vamos saber se um numero é par ou impar')
numero = int(input("digite um numero:"))

if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é impar")

'''

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
  
'''
import datetime

data = datetime.datetime.now()

agora = data.hour
print(f'data e hora :  {data}')

if agora > 0 and agora < 12:
    print('bom dia')
elif agora >=12 and agora <= 17:
    print('boa tarde')
elif agora <= 18 and agora <= 23:
  print('boa noite')
'''

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

'''
nome = input('Qual o seu nome? :')

numero_Nome = len(nome)

if numero_Nome <= 4:
    print(f"Seu nome tem {len(nome)} letras")
    print('seu nome é muito curto')
elif numero_Nome >= 5:
    print(f"Seu nome tem {len(nome)} letras")
    print('seu nome é muito grande')
'''