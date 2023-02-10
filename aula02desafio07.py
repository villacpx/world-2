import math
print('LER UM NÚMERO E MOSTRAR SE É NÚMERO PRIMO OU NÃO')
n = int(input('Digite um número: '))
for c in range(1, n+1,):
    print(c)
if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
    print('Esse é um número primo!')
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0:
    print('esse não é um número primo!')
else:
    print('esse é um número primo!')
