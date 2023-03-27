"""
A expressão not faz com que a variável se inverta. Quando eu coloco ”not senha”  se a variável senha vier vazia vai cair no laço.
Ela tambem faz com bollean true vire false.
"""

senha = input('digite a senha: ')

if not senha :
    print('erro! Campo vazio!')
elif senha == '123456789' :
    print("Bem vindo".upper())
