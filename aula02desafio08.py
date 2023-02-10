print('PROGRAMA QUE VERIFICA SE É UM PALÍNDROMO DESCONSIDERANDO OS ESPAÇOS')
frase = str(input('Digite uma frase: '))
frase = frase.strip().lower()
frase3 = frase.split()
frase2 = (''.join(frase3))
b = (frase2[::-1])
c = bool(frase2 == b)
print('-='*20)
if frase2 == b:
    print('Isso é um palíndromo')
    print('-='*20)
elif frase2 != b:
    print('Isso não é um palíndromo')
    print('-='*20)
# 'Na minha versão não consegui colocar a repetição, e pesquisando consegui achar somente a forma [::-1]'
# 'a questão foi resolvida porém não correta.'

print('-'*20)
print('VERSÃO DO GUANABARA')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto)
print(inverso)
if inverso == junto:
    print('É UM PALÍNDROMO')
elif inverso != junto:
    print('NÃO É UM PALÍNDROMO')
