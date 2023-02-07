print('PRESTAÇÃO DE UMA CASA')
casa = float(input('Digite o valor da casa: '))
salario = float(input('Qual é o seu salário mensal? '))
anos = int(input('Em quantos anos quer pagar? '))
meses = anos * 12
valormensal = casa/meses
print(f'A prestação da sua casa será de R${valormensal:.2f}')
orçamento = (salario*130)/100 - salario
if valormensal < orçamento:
    print('Seu orçamento está aprovado! Ligue para a nossa agência para saber mais.')
elif valormensal == orçamento:
    print('Seu orçamento foi aprovado porém contém riscos, ligue para a nossa agência para saber mais.')
else:
    print('Seu orçamento foi reprovado, caso queira resolver seu problema ligue para nosso SAC!')
