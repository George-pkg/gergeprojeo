import time
maior = 0
nomeX = ''
mm = 0
media = 0
for id in range(1, 5):
    nome = str(input('Digite o {}º nome a se analisar: '.format(id)))
    idade = int(input('Digite a idade do cliente: '))
    sexo = str(input('Digite o sexo do cliente (M/F): ')).upper()
    print('')
    media += idade
    if id == 1 and sexo == 'M':
        maior = idade
        nomeX = nome
    else:
        if sexo == 'M':
            if idade > maior:
                maior = idade
                nomeX = nome
        elif sexo == 'F':
            if idade < 20:
                mm += 1
print('\033[34mANALISANDO DADOS...\033[m')
time.sleep(3)
print('A media de idade dos participantes é {} anos.'.format(media // 4))
print('O nome do homem mais velho é {}, com {} anos.'.format(nomeX, maior))
if mm == 0:
    print('O programa não constatou nenhuma mulher com menos de 20 anos.')
elif mm == 1:
    print('O programa só constatou apenas uma mulher com menos de 20 anos.')
else:
    print('O programa constatou {} mulheres com menos de 20 anos.'.format(mm))