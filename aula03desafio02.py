import random
computador = random.randint(0, 10)
jogador = -1
tentativas = 1
while jogador != computador:
    r = int(input('De 0 a 10, tente adivinhar o número em que o computador está pensando: '))
    while r != computador:
        r = int(input('TENTE NOVAMENTE: '))
        tentativas += 1
    jogador = r
if tentativas == 1:
    print('PARABÉNS, VOCÊ ACERTOU DE PRIMEIRA')
elif tentativas != 1:
    print(f'PARABÉNS, VOCÊ ACERTOU COM {tentativas} TENTATIVAS')
