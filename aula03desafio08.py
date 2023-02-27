n = 0
n3 = 0
contagem = 0
print('-'*20)
print('Quando quiser finalizar o programa, Digite 999')
print('-'*20)
while n != 999:
    n2 = int(input('Digite um número: '))
    n = n2
    n3 += n2
    contagem += 1
n3 -= 999
print(f'A quantidade de números digitados é {contagem-1}')
if n3 == 0:
    print('O resultado foi 0')
else:
    print(f'E a soma de todos eles é: {n3-999}')
