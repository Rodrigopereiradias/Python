def principal():
    peso = float(input('peso (kg): '))
    altura = float(input('altura (m): '))

    imc = peso / (altura ** 2)
    print(f'Seu IMC é: {imc}')



principal()