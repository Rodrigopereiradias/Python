frase = str(input("Digite uma frase: ").strip().upper())
letra = str(input("Qual letra quer contar: ").strip().upper())
print("A letra {} apreceu {}".format(letra, frase.count('A')))
print("A primeira letra {} apareceu na posição {}".format(letra, frase.find('A')+1))
print("A ultima letra {} apareceu na posição {}".format(letra, frase.rfind('A')+1))
