matriz = [[0, 0, 0], [0, 0 ,0], [0, 0, 0]]
pares = ter = seguido = 0
for g1 in range(0, 3):
    for g2 in range(0, 3):
        matriz[g1][g2] = int(input(f'Digite um número para colocar na coluna [{g1}, {g2}]: '))
print('-=' * 30)
for g1 in range(0, 3):
    for g2 in range(0, 3):
        print(f'[{matriz[g1][g2]:^5}]', end='')
    print('')
print('-=' * 30)
for g1 in range(0, 3):
    for g2 in range(0, 3):
        if matriz[g1][g2] % 2 == 0:
            pares = matriz[g1][g2] + pares
        if g2 == 2:
            ter = matriz[g1][g2] + ter
        if g1 == 1:
            if g2 == 0 or matriz[g1][g2] > seguido:
                seguido = matriz[g1][g2]
print(f'A soma dos números pares da matriz é {pares}.\n'
      f'A soma dos números da terceira coluna é {ter}.\n'
      f'O maior número da segunda fileira é {seguido}.')