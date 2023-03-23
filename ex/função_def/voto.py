def cor(palavra, cor):
    if cor == 'vermelho':
        core = f'\033[31m{palavra}\033[m'
        return core
    if cor == 'verde':
        core = f'\033[32m{palavra}\033[m'
        return core
    if cor == 'amarelo':
        core = f'\033[33m{palavra}\033[m'
        return core


def voto(num):
    num = 2022 - num
    if num < 18:
        print(f'Usuario com {num} anos de idade: {cor("NÃO VOTA", "amarelo")}')
    if 18 <= num < 65:
        print(f'Usuario com {num} anos de idade: {cor("VOTO OBRIGATORIO", "vermelho")}')
    if num > 65:
        print(f'Usuario com {num} anos de idade: {cor("VOTO OPCIONAL", "amarelo")}')


set = int(input('Ano de nascimento: '))
voto(set)
