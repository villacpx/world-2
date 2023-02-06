import random
a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
print(a, b, c)
if a < b + c and b < a + c and c < a + b:
    print('essas medidas conseguem formar um triângulo!')
    if a == b and b == c and c == a:
        print('Esse triângulo é um equilátero')
    elif a == b or b == c or c == a:
        print('Esse triângulo é um isósceles')
    else:
        print('Esse triângulo é um escaleno')

else:
    print('Essas medidas não formam um triângulo!')
