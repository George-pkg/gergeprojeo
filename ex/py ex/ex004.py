homens = maiores = mulheres = 0
while True:
    print('____________________________\n'
          '    CADASTRE UMA PESSOA\n'
          '____________________________')
    while True:
        idade = int(input('Idade: '))
        if idade > 0 and idade < 150:
            break
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()
        if sexo == 'F' or sexo == 'M':
            break
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
         if idade < 20:
            mulheres += 1
    print('____________________________')
    while True:
        jogo = str(input('Quer continuar? [S/N] ')).upper()
        if jogo == 'N' or jogo == 'S':
            break
    if jogo == 'N':
        break
print('\n==========FIM DO PROGRAMA==========\n')
print(f'Total de pessoas com mais de 18 anos: {maiores}')
if homens == 1:
    print('Ao todo temos apenas um homem casdastrado.')
elif homens == 0:
    print('Não encontramos nenhum homem cadastrado no sistema.')
else:
    print(f'Ao todo temos {homens} cadastrados.')
if mulheres == 1:
    print('E temos apenas uma mulher com menos de 20 anos')
elif mulheres == 0:
    print('Não encontramos nenhuma mulher com menos de 20 anos cadastrada no sistema.')
else:
    print(f'E temos {mulheres} mulheres com menos de 20 anos')