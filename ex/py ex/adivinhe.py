import random
import time
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('tente adivinhar em qual numero estou pensando de 1 a 10')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
nv = int(input(':'))
mm = random.randint(0, 9)
m = mm + 1
tentativa = 1
print('pensando...')
time.sleep(2)
while m != nv:
    tentativa += 1
    if m > nv:
        nv = int(input('\n'
              'você errou, tente um número maior: '))
    if m < nv:
        nv = int(input('\n'
              'você errou, tente um número menor: '))
print('\n'
      '-=-=-=-=-=-VOCÊ ACERTOU-=-=-=-=-=-')
print(' (você acertou com {} tentativas)'.format(tentativa))