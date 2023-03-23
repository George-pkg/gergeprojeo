dice = dict()
goal = list()
dice['nome'] = str(input('Nome do jogador: '))
limit_f = int(input(f'Quantos jogos {dice["nome"]} jogou: '))
limit_i = toti = 0
while True:
    if limit_f != limit_i:
        g = int(input(f'Quantos gols na partida {limit_i + 1}: '))
        goal.append(g)
        limit_i += 1
        toti += g
    else:
        break
print('-=' * 30)
dice['gols'] = goal[:]
dice['total'] = toti
print(dice)
print('-=' * 30)
for n, name in enumerate(dice):
    print(f'O campo {name} tem o valor de {dice[name]}.')
print('-=' * 30)
if toti == 1:
    print(f'O jogador {dice["nome"]} jogou apenas uma partida')
if toti > 1:
    print(f'O jogador {dice["nome"]} jogou {dice["total"]} partidas.')
    for n, name in enumerate(goal):
        print(f'    => Na  partida {n + 1}, fez {name} gols.')
    print(f'Foi um total de {toti} de gols.')