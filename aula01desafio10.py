import random
j1 = 1
j2 = 2
j3 = 3
#j1 = pedra
#j2 = papel
#j3 = tesoura
jogadas = [j1, j2, j3]
jogadas = random.choice(jogadas)
print(str('1 - PEDRA\n2 - PAPEL\n3 - TESOURA'))
escolha = int(input('Digite sua opção: '))
if escolha == jogadas:
    print('VOCÊS EMPATARAM')
elif escolha == 1 and jogadas == j3:
    print('VOCÊ JOGOU PEDRA E GANHOU!')
elif escolha == 2 and jogadas == j1:
    print('VOCÊ JOGOU PAPEL E GANHOU!')
elif escolha == 3 and jogadas == j2:
    print('VOCÊ JOGOU TESOURA E GANHOU')
else:
    print('VOCÊ PERDEU!')
print(jogadas)

print('FORMA DO GUANABARA')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('SUAS OPÇÕES\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('JOGADA INVÁLIDA')