lidade = []
maioridade = 0
lnome = []
nomevelho = []
novinhas = 0
sidade = 0
midade = 0
for p in range(1, 5):
    print('1 - MASCULINO\n2 - FEMININO')
    mf = int(input(''))
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sidade += idade
    if p == 1:
        lidade.append(idade)
        maioridade = idade
        if mf == 2 and idade < 20:
            novinhas += 1
    else:
        lidade.append(idade)
        if idade > maioridade:
            maioridade = idade
            if mf == 1:
                nomevelho.append(nome)
        if mf == 2 and idade < 20:
            novinhas += 1
midade = sidade / 4
print(f'O nome do homem mais velho é: {nomevelho}')
if novinhas == 0:
    print(f'Não tem mulheres abaixo de 20 anos')
elif novinhas != 0:
    print(f'A quantidade de mulheres abaixo de 20 anos é: {novinhas}')
print(f'A media de idade do grupo é de {midade} anos')
# CORREÇÃO
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for p in range(1, 5):
    nome2 = str(input('Nome: ')).strip()
    idade2 = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade2
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade2
        nomemaisvelho = nome2
    if sexo in 'Mm' and idade2 > maioridadehomem:
        maioridadehomem = idade2
        nomemaisvelho = nome2
    if idade2 < 20 and sexo in 'Ff':
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'O homem mais velho é {nomemaisvelho} com seus {maioridadehomem} anos!')
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'{totmulher20} mulheres possuem idade abaixo de 20 anos')
