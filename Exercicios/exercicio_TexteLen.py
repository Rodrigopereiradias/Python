'''Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
'''

def teste():
        
        nome = input('Qual o seu primero nome?: ')
        idade = input('qual sua idade?: ')
        
        if nome and idade:

            print(f'seu nome é :{nome}')
            print(f'sua idade é : {idade}')
            print(f'seu nome tem {len(nome)} letras')
            print(f'seu nome ao contrario é: {nome[::-1]}')
            if " " in nome:
                print("seu nome tem espaços")
            else:
                print("seu nome não tem espaços")
        else:

            print('houve um problema! tente novamente')
            teste()
           
teste()