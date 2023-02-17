pesomin = 0
pesomax = 0
for p in range(1, 7):
    pp = float(input('Digite o peso: '))
    if p == 1:
        pesomin = pp
        pesomax = pp
    else:
        if pp > pesomax:
            pesomax = pp
        if pp < pesomin:
            pesomin = pp
print(f'peso maior {pesomax}')
print(f'peso menor {pesomin}')
# 'não consegui completar, porém aprendi a como funciona o resgistro de uma variável sobre a repetição'
