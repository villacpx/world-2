sexu = ''
while sexu != 'F' and sexu != 'M':
    sexo = str(input('DIGITE SEU SEXO [M|F]: ')).strip().upper()
    sexu = sexo
    if sexo == 'M':
        print('SEXO ESCOLHIDO: MASCULINO')
    if sexo == 'F':
        print('SEXO ESCOLHIDO: FEMININO')
    elif sexo != 'M' and sexo != 'F':
        print('ERRO! TENTE NOVAMENTE.')
