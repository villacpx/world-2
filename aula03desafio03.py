from time import sleep
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
print('\n')
omenu = 0
while omenu != 5:
    print(' [1] SOMA \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA')
    print('\n')
    omenu = int(input('SELECIONE A OPÇÃO: '))
    sleep(0.5)
    if omenu == 1:
        soma = n1 + n2
        print('-'*20)
        print(f'A SOMA ENTRE {n1} E {n2} É DE: {soma}')
        print('-'*20)
        sleep(1.5)
        print('\n')
    if omenu == 2:
        multi = n1 * n2
        print('-'*20)
        print(f'A MULTIPLICAÇÃO ENTRE {n1} E {n2} É DE: {multi}')
        print('-'*20)
        sleep(1.5)
        print('\n')
    if omenu == 3:
        print('-'*20)
        if n1 > n2:
            print(f'O MAIOR NÚMERO É {n1} E O MENOR É O {n2}.')
        elif n2 > n1:
            print(f'O MAIOR NÚMERO É {n2} E O MENOR É O {n1}')
        print('-'*20)
        sleep(1.5)
        print('\n')
    if omenu == 4:
        print('-'*20)
        n1 = int(input('DIGITE O 1° NÚMERO: '))
        n2 = int(input('DIGITE O 2° NÚMERO: '))
        print('-'*20)
        sleep(1.5)
        print('\n')
    elif omenu != 1 and omenu != 2 and omenu != 3 and omenu != 4 and omenu != 5:
        print('\n')
        print('ERRO, TENTE NOVAMENTE!')
        print('\n')
print('OBRIGADO POR USAR O NOSSO PROGRAMA! =)')
