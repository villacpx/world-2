n = int(input('Digite um número: '))
QuantidadeTermos = n
TermoInicial = 0
n2 = int(n)
n3 = 0
n4 = 0
print(n)
print(n2)
while TermoInicial != QuantidadeTermos:
    TermoInicial += 1
    n3 = n + n2
    print(n3)
    n4 = n3 + n2
    print(n4)
    n2 = n3 + n4
    print(n2)
    n3 = n2 + n4
    print(n3)
