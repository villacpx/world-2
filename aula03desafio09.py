pergunta = str('')
n1 = 0
media = 0
soma = 0
maior = 0
menor = 0
ResultadoMedia = 0
while pergunta != str('N'):
    n1 = int(input('Digite um número: '))
    if media == 0:
        maior = n1
        menor = n1
    media += 1
    pergunta = str(input('Quer continuar? [S/N] ')).upper()
    if pergunta != 'N' and pergunta != 'S':
        print('ERRO, TENTE NOVAMENTE')
        pergunta = str(input('Quer continuar? [S/N] ')).upper()
    soma += n1
    ResultadoMedia = soma / media
    if maior < n1:
        maior = n1
    if n1 < menor:
        menor = n1
print(f'Essa é a média {ResultadoMedia}')
print(f'Esse número é o menor: {menor}, e o número maior é: {maior}')
