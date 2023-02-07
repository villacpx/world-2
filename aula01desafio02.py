print('Conversor')
n1 = int(input('Digite um número: '))
n2 = int(input('OPÇÕES: DIGITE 1 P/ BINÁRIO, 2 P/ OCTAL E 3 P/ HEXADECIMAL: '))
#binário =
#octal =
#hexadecimal =
if n2 == 1:
    print(f'Sua conversão para número binário está aqui: {bin(n1)}')
elif n2 == 2:
    print(f'Aqui está, sua conversão para um número octal: {oct(n1)}')
elif n2 == 3:
    print(f'pronto, aqui está sua conversão para número hexadecimal: {hex(n1)}')
