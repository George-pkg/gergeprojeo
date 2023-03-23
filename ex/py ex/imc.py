print('\033[35m=-=-=-=-=-=-=-=-=-=\n'
      '=  TABELA DO IMC  =\n'
      '=-=-=-=-=-=-=-=-=-=\033[m ')
at = float(input('Digite sua altura: '))
ps = float(input('digite seu peso: '))
imc = ps / (at * at)
print('')
if imc < 18.5:
    print('Você esta \033[33m ABAIXO DO PESO\033[m')
elif imc >= 18.5 and imc < 25:
    print('Você esta com o \033[32mPESO IDEAL\033[m')
elif imc >= 25 and imc < 30:
    print('Você esta com \033[33mSOBREPESO\033[m')
elif imc >= 30 and imc < 35:
    print('Você esta com \033[31mOBESIDADE GRAU 1\033[m')
elif imc >= 35 and imc < 40:
    print('Você esta com \033[31mOBESIDADE GRAU 2\033[m')
else:
    print('Você esta com \033[31mOBESIDADE GRAU 3\033[m')