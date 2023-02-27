PrimeiroTermo = int(input('DIGITE O PRIMEIRO TERMO DA PA: '))
SegundoTermo = int(input('DIGITE A RAZÃO DESSA PA: '))
start = 1
PA = 0
print(f'{PrimeiroTermo}')
while start != 10:
    PA = PrimeiroTermo + SegundoTermo
    PrimeiroTermo = PA
    print(f'{PrimeiroTermo}')
    start += 1
