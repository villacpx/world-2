import random
from datetime import date
menores = 0
maiores = 0
for c in range(0, 7):
    n = random.randint(2000, 2020)
    print(n)
    if (date.today().year - n) < 18:
        menores += 1
    elif (date.today().year - n) > 18:
        maiores += 1

print(f'A quantidade de menores é {menores}')
print(f'A quantidade de maiores é {maiores}')
# 'Com a correção, consegui entender que o += somente 1 = faz uma variável receber algo ou comando'
# 'o + faz uma adição ou seja recebe mais 1, aula complicada e me fez quebrar bastante a cabeça'
# 'uma grande derrota também te dá um bom aprendizado e experiência'
