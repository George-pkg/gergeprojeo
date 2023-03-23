import random, time
s = 0
while True:
    pc = random.randint(1, 3)
    gg = str(input('Escolha entre ímpar ou par:(i/p) ')).upper()
    jg = int(input('Digite um número para jogar:'))
    time.sleep(1)
    print('maquina sorteando número...')
    time.sleep(2)
    print('....')
    time.sleep(2)
    if gg == 'P':
        if (pc + jg) % 2 == 0:
            print(f'jogador jogou {jg} e o conputador jogou {pc},\n'
                  f'\033[32mJOGADOR VENCE!!!\033[m')
            s += 1
        else:
            print(f'jogador jogou {jg} e o conputador jogou {pc},\n'
                  f'\033[34mJOGADOR PERDE :( :( :(\033[m')
            break
    if gg == 'I':
        if (pc + jg) % 2 == 0:
            print(f'jogador jogou {jg} e o conputador jogou {pc},\n'
                  f'\033[34mJOGADOR PERDE :( :( :(\033[m')
            break
        else:
            print(f'jogador jogou {jg} e o conputador jogou {pc},\n'
                  f'\033[32mJOGADOR VENCE!!!\033[m')
            s += 1
print('')
if s == 0:
    print('O jogador não conseguiu ganhar nenhuma partida.')
elif s == 1:
    print('O jogador só ganhou uma partida, por sorte ;)')
else:
    print(f'O jogador conseguiu ganhar {s} vitorias consecutivas...\n'
          f'você tem sorte em :) :0')