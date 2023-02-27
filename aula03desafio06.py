PrimeiroTermo = int(input('Digite o primeiro termo dessa PA: '))
SegundoTermo = int(input('Digite a razão dessa PA: '))
start = 1
PA = 0
NovosTermos = 0
pergunta1 = ''
print(PrimeiroTermo)
while start != 10:
    PA = PrimeiroTermo + SegundoTermo
    PrimeiroTermo = PA
    start += 1
    print(PrimeiroTermo)
while pergunta1 != 'N' and pergunta1 != 'S':
    pergunta1 = str(input('Você quer saber mais termos? [S/N] ')).upper().strip()
    if pergunta1 == 'N':
        print('Obrigado por usar nosso programa!')
    elif pergunta1 == 'S':
        NovosTermos = int(input('Quantos termos a mais você quer? '))
        start = 0
        if NovosTermos != 0:
            while start != NovosTermos:
                PA = PrimeiroTermo + SegundoTermo
                PrimeiroTermo = PA
                start += 1
                print(PrimeiroTermo)
    else:
        print('ERRO, TENTE NOVAMENTE')
