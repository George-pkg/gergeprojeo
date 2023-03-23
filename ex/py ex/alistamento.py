import datetime
print('\033[34m')
print('=-=-=-=-=-=-=-=-=-=\n'
      '=-  alistamento  -=\n'
      '=-=-=-=-=-=-=-=-=-=')
print('\033[m')
a = int(input('Qual seu ano de nascimento: '))
ano = datetime.date.today().year - a
print('')
print('quem nasceu em {} tem {} anos'.format(a, ano))
if ano >= 18:
      if ano == 18:
            print('você \033[4mpode\033[m e \033[4mdeve\033[m se alistar esse ano')
      if ano > 18:
            if ano == 19:
                print('já passou do ano de você se alistar\n'
                  'era pra você ter se alistado a {} ano'.format(ano - 18))
            else:
                print('já passou do ano de você se alistar\n'
                  'era pra voce ter se alistado a {} anos atras'.format(ano - 18))
else:
       if ano == 17:
            print('Ainda não esta no tempo de se alistar,\n'
                  'pois falta {} ano'.format(18 - ano))
            print('você só podera se alistar em {}'.format((18 -ano) + 2021))
       else:
           print('Ainda não esta no tempo de se alistar,\n'
                 'pois falta {} anos'.format(18 - ano))
           print('você só podera se alistar em {}'.format((18 - ano) + 2021))