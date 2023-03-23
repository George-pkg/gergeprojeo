v = int(input('qual a velocidade atual do carro? '))
l = int(80)
if v <= l:
    print('\033[1;32mTenha um bom dia! Dirija com segurança!\033[m')
else:
    print('\033[1;31mMULTADO, Você escedeu a velocidade permitido que é de 80K/h')
    mult = (v - 80) * 7
    print('Você deve pagar uma multa de\033[m\033[1;33m R${:.2f}!\033[m'.format(mult))
