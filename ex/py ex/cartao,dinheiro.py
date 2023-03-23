d = float(input('Qual o preço a se pagar? R$'))
pr = str(input('\nVocê vai pagar no dinheiro ou no cartão? '))
print('')
if pr == 'dinheiro' :
    print('ao pagar com dinheiro você tem \033[32m10%\033[m de desconto,\n'
          'e o preço final a se pagar é \033[32mR${:.2f}\033[m'.format(d * 0.9))
elif pr == 'cartao':
    pp = int(input('Você vai querer parcelar?\n'
          'pois se você pagar a vista tera \033[4;32m5%\033[m de desconto\n'
          'e se pagar com \033[4m2x de parcela\033[m, será o preço normal\n'
          'e com \033[4m3x de parcela\033[m ira ter um juros de \033[4;31m20%\033[m\n'
                   'Qual é sua escolha: '))
    print('')
    if pp == 1:
        print('Você escolheu pagar a vista,\n'
              'assim o preço fica \033[32mR${:.2f}\033[m'.format(d * 0.95))
    elif pp == 2:
        print('Você escolheu pagar com 2x de parcela,\n'
              'assim o preço fica \033[32mR${:.2f}\033[m'.format(d))
    elif pp == 3:
        print('Você escolheu pagar com 3x de parcela,\n'
              'assim o preço com juros fica \033[32mR${:.2f}\033[m'.format(d + (d * 0.2)))