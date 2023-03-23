escrito = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while True:
    if num >= 0 and num <= 20:
       print('Você digitou o número {}'.format(escrito[num]))
       break
    else:
        num = int(input('Tente novamente. Digite um número entre 0 e 20:'))
