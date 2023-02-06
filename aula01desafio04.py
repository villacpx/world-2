from datetime import date
print('Alistamento Militar')
ano = int(input('Digite seu ano de nascimento: '))
dia = date.today().year
idade = dia-ano
n1 = idade-18
n2 = 18-idade
if idade == 18:
    print('Esse ano você deve comparecer no serviço militar!')
elif idade > 18:
    print(f'Já passou {n1} ano(s) que você deveria ter se alistado.')
elif idade < 18:
    print(f'Ainda falta {n2} ano(s) para você se alistar')
