from datetime import date
ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
n1 = atual-ano
if 0 < n1 <= 9:
    print('CATEGORIA MIRIM')
elif 9 < n1 <= 14:
    print('CATEGORIA INFANTIL')
elif 14 < n1 < 19:
    print('CATEGORIA JUNIOR')
elif 19 <= n1 <= 20:
    print('CATEGORIA SENIOR')
elif 20 < n1:
    print('CATEGORIA MASTER')
