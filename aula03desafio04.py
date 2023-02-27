numero = int(input('Digite um número: '))
fatorial = numero
respostaFinal = 0
multi = 0
while fatorial != 1:
    eq = fatorial - 1
    fatorial = eq
    multi = numero * fatorial
    numero = multi
    respostaFinal = numero
print(f'O FATORIAL DESTE NÚMERO É: {respostaFinal}')
