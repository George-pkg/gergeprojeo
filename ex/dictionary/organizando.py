import random, time, operator
#dice = dados
dice = {'jogador_1': random.randint(1, 6),
        'jogador_2': random.randint(1, 6),
        'jogador_3': random.randint(1, 6),
        'jogador_4': random.randint(1, 6)
}
ranking = list()
print('Valores sorteados: ')
for j, n in dice.items():
    print(f'O {j} jogou o dado e caiu o número {n}')
    time.sleep(1)
ranking = sorted(dice.items(), key=operator.itemgetter(1), reverse=True)
print(ranking)
print('-=' * 20)
for i, k in enumerate(ranking):
    print(f'{i + 1}° lugar: {k[0]} com {k[1]}')
    time.sleep(1)
