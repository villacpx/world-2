peso = float(input('Digite seu peso, ex 69.84: '))
altura = float(input('Digite sua altura, ex 1.70: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print('PESO IDEAL')
elif 25 < imc <= 30:
    print('SOBREPESO')
elif 30 < imc <= 40:
    print('OBESIDADE')
elif 40 < imc:
    print('OBESIDADE MÓRBIDA')
