print('TV R$1900, COM 10% DE DESCONTO À VISTA EM DINHEIRO OU CHEQUE\n NO CARTÃO À VISTA O DESCONTO É DE 5%')
forma = int(input('DE QUE FORMA PENSA EM PAGAR?\n 1- À VISTA \n 2- PARCELADO \n '))
desconto10 = float(1900 - ((1900*10)/100))
desconto5 = float(1900 - ((1900*5)/100))
if forma == 1:
    forma2 = int(input(' 1- Dinheiro \n 2- Cheque \n 3- Cartão \n '))
    if forma2 == 1 or forma2 == 2:
        print(f'Com o desconto de 10%, o valor final de sua compra ficou {desconto10}, ok?')
    elif forma2 == 3:
        print(f'Com o desconto de 5%, o valor final de sua compra ficou {desconto5}, ok?')

if forma == 2:
    vezes = int(input('Em quantas vezes você pretende fazer? a partir de 3x nós cobramos 20% de juros!! '))
    valorfinal = float(1900 + (1900 * 20)/100)
    parcelas = float(valorfinal / vezes)
    if vezes == 2:
        print(f'Então ficará {vezes} parcelas de R$950.00, Ok?')
    elif 3 <= vezes:
        print(f'Ficarão {vezes} de R${parcelas:.2f}, Ok?')
