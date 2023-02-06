print('Número maior, menor e igual')
import random
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
if n1 > n2:
    print(f'O {n1} é o maior número, e o {n2} é o menor número!')
elif n2 > n1:
    print(f'O maior número é o {n2}, e o menor é o {n1}')
elif n1 == n2:
    print(f'Os dois são iguais!!')
