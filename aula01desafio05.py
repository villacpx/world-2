nota1 = float(input('Digite a nota do primeiro trimestre: '))
nota2 = float(input('Digite agora a nota do segundo trimestre: '))
media = (nota1+nota2)/2
if media > 7.0:
    print('APROVADO')
elif 5 < media < 6.9:
    print('RECUPERAÇÃO')
elif media < 5.0:
    print('REPROVADO')
