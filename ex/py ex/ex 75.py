num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
       int(input('Digite outro número: ')), int(input('Digite outro número: ')))
if num.count(9) > 0:
       print(f'\no número nove aparece {num.count(9)} vezes.')
else:
       print('O número nove naão aparece nenhuma vez.')
if num.count(3) > 0:
       print(f'O número 3 apareceu na {num.index(3) + 1}° colocação.')
else:
       print('o número 3 não foi digitado.')
print('\nOs números pares sao :')
for c in num:
       if c % 2 == 0:
              print(c, end=',')