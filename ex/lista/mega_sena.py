import random, time
print('-' * 40)
print('JOGO NA MEGA SENA'.center(40))
print('-' * 40)
jogos = int(input('Dígite o número de jogos que você quer sortear: '))
if jogos == 1:
    print('-=-=-=', f'SORTEANDO {jogos} JOGO'.center(5), '-=-=-=')
else:
    print('-=-=-=', f'SORTEANDO {jogos} JOGOS'.center(5), '-=-=-=')
list_game = list()

for n in range(0, jogos):
    cont = 0
    time.sleep(1.5)
    while True:
        if cont <= 6:
            l = random.randint(0, 60)
            list_game.append(l)
            cont += 1
        else:
            break
    list_game.sort()
    print(f'JOGO {n + 1}°: ', list_game)
    list_game.clear()
print('-=-=-=-= < BOA SORTE > -=-=-=-=')