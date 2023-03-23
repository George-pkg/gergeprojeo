ca = float(input('Digite o valor do imóvel do seu interesse: R$'))
sa = float(input('Digite seu salário por mês: R$'))
temp = int(input('Em quantos anos pretende pagar o imóvel :'))
min = sa * 0,2
prest = ca / (temp * 12)
print('\n\033[94mPara pagar uma casa de \033[32mR${:.2f}\033[m\033[94m em {} anos'.format(ca, temp))
print('A prestação será de \033[32mR${:.2f}\033[m\033[94m por mês.'.format(prest))
if prest > sa:
    print('\033[33m\nEMPRESTIMO NEGADO\033[m')
if prest <= sa:
    print('\033[32m\nEMPRESTIMO VALIDO\033[m')
