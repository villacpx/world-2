nome = str(input('Qual é o seu nome? '))
if nome == 'Nathan':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Enzo' or nome == 'Valentina':
    print('Eita geraçãozinha!')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Que belo nome a senhorita tem!')
else:
    print('Que nome normal')
print(f'Tenha um bom dia, {nome}!')
