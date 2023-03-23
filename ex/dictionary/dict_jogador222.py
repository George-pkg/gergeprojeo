dice = dict()
gg = list()
total_dice = list()
quest = 'Y'
while True:
    if quest == 'Y':
        print('-' * 20)
        dice['nome'] = str(input('Nome do Jogador: ')).upper()
        limit_f = int(input(f'Quantas partidas {dice["nome"]} jogou? '))
        limit_i = 1
        while True:
            if limit_i != limit_f:
                g = int(input(f'Qantos gols na partida {limit_i}'))
                gg.append(g)
                limit_i += 1
            if limit_i == limit_f:
                dice['gols'] = gg[:]
                break
    quest = str(input('Quer continuar? [Y/N] ')).upper()
    total_dice.append(dice.copy())
    if quest == 'N':
        break
print('-=' * 30)
print('cod  nome                                  gols             total')