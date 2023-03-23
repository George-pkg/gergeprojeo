import random
import pygame, random, time
from pygame.locals import *
vitorias = derrotas = empate = 0
while True:
    print('=-' * 15,
          '\n=     JOGOS DISPONIVES       ='
          '\n=                            ='
          '\n=JOKENPOR_________________[1]='
          '\n=JOGO DO ADIVINHA_________[2]='
          '\n=PAR OU ÌMPAR_____________[3]='
          '\n=SNAKE(PROTOT)____________[4]='
          '\n=PLACAR DE PONTAÇÂO_______[5]='
          '\n=EXTRA____________________[6]='
          '\n=SAIR DO PROGRAMA_________[7]=\n',
          '=-' * 15 )
    cd = int(input('escolha seu modo de jogo :'))

    while cd == 1:
        pc = random.randint(1, 3)
        #1 papel+
        #2 pedra
        #3 tesousa
        print('\n', '=-' * 15)
        print('[1]PAPEL\n'
              '[2]PEDRA\n'
              '[3]TESOURA')
        print('=-' * 15, '\n')
        jg = int(input('Digite sua escolha: '))
        time.sleep(1)
        print('\033[35mJO')
        time.sleep(1)
        print('\033[34mKEN')
        time.sleep(2)
        print('\033[1;36mPOOO!!!\n')
        if jg == 1:
            if pc == 1:
                empate += 1
                print('O jogador escolheu \033[4mPAPEL\033[1;36m.\n'
                      'E o computador tambem escolheu \033[4mPAPEL\033[1;36m...\n'
                      'ai temos um \033[33mEMPATE\033[m')
            elif pc == 2:
                vitorias += 1
                print('O jogador escolheu \033[4mPAPEL\033[1;36m.\n'
                      'E o computador escolheu \033[4mPEDRA\033[1;36m...\n'
                      '     \033[32mVITORIA DO JOGADOR!!!\033[m')
            elif pc == 3:
                derrotas += 1
                print('O jogador escolheu \033[4mPAPEL\033[1;36m\n'
                      'E o computador escolheu escolheu \033[4mTESSOURA\033[1;36m...\n'
                      '     \033[34mVITORIA DO COMPUTADOR\033[m')
            else:
                print('ERRORR, OPÇÂO INVALIDA')
        elif jg == 2:
            if pc == 1:
                derrotas += 1
                print('O jogador escolheu \033[4mPEDRA\033[m.\n'
                      'E o computador escolheu \033[4mPAPEL\033[m...\n'
                      '     \033[34mVITORIA DO COMPUTADOR\033[m')
            elif pc == 2:
                empate += 1
                print('O jogador escolheu \033[4mPEDRA\033[m.\n'
                      'E o computador tambem escolheu \033[4mPEDRA\033[m...\n'
                      'ai temos um \033[33mEMPATE\033[m')
            elif pc == 3:
                vitorias += 1
                print('O jogador escolheu \033[4mPEDRA\033[m.\n'
                      'E o computador escolheu \033[4TESOURA\033[m...\n'
                     '     \033[33mVITORIA DO JOGADOR!!!\033[m')
            else:
                print('ERRORR, OPÇÂO INVALIDA')
        elif jg == 3:
            if pc == 1:
                derrotas += 1
                print('O jogador escolheu \033[4mTESSOURA\033[m.\n'
                      'E o computador escolheu \033[4mPAPEL\033[m...\n'
                      '     \033[32mVITORIA DO JOGADOR!!!\033[m')
            elif pc == 2:
                empate += 1
                print('O jogador escolheu \033[4mTESSOURA\033[m.\n'
                      'E o computador escolheu \033[4mPEDRA\033[m...\n'
                      '     \033[34mVITORIA DO COMPUTADOR\033[m')
            elif pc == 3:
                vitorias += 1
                print('O jogador escolheu \033[4mTESSOURA\033[m.\n'
                      'E o computador tambem escolheu \033[4mTESOURA\033[m...\n'
                      'ai temos um \033[33mEMPATE\033[m')
            else:
                print('ERRORR, OPÇÂO INVALIDA')
        else:
            print('ERRORR, OPÇÂO INVALIDA')
        sair = str(input('QUER JOGAR NOVAMENTE? (Y/N)')).upper()
        if sair == 'N':
            break

    while cd == 2:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('tente adivinhar em qual numero estou pensando de 1 a 10')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        nv = int(input(':'))
        mm = random.randint(0, 9)
        m = mm + 1
        tentativa = 1
        print('pensando...')
        time.sleep(2)
        while m != nv:
            tentativa += 1
            if m > nv:
                nv = int(input('\n'
                               'você errou, tente um número maior: '))
            if m < nv:
                nv = int(input('\n'
                               'você errou, tente um número menor: '))
        print('\n'
              '-=-=-=-=-=-VOCÊ ACERTOU-=-=-=-=-=-')
        print(' (você acertou com {} tentativas)'.format(tentativa))
        a = str(input('Deseja continuar jogando esse jogo? (y/n)')).upper()
        if a == 'N':
            break

    while cd == 3:
        vi = 0
        while True:
            ip = str(input('Escolha entre impar ou par: ')).upper()
            lp = int(input('Agora escolha um número para jogar: '))
            pc = random.randint(1, 2)
            jg = lp + pc
            print('COMPUTADOR PENSANDO....\n')
            time.sleep(1)
            print('SUSPENSE....\n')
            time.sleep(2)
            if ip == 'I':
                if jg % 2 == 0:
                    print(f'você jogou {lp} e o computador {pc}. Total de {lp + pc} deu PAR')
                    print('O jogador perdeu.... :( \n'
                          'assim acabou com suas vidas..\n')
                    if vi == 1:
                        print('Você conseguiu ganha apenas uma vez')
                    if vi > 1:
                        print(f'Você conseguiu {vi} vitorias consecutivas')
                    break
                else:
                    vi += 1
                    print(f'você jogou {lp} e o computador {pc}. Total de {lp + pc} deu IMPAR')
                    print('O jogador ganhou.... :)')
                    retu = str(input('Jogar novamente? ')).upper()
                    if retu == 'N':
                        if vi == 1:
                            print('Você conseguiu ganha apenas uma vez')
                        if vi > 1:
                            print(f'Você conseguiu {vi} vitorias consecutivas')
                        break
            elif ip == 'P':
                if jg % 2 == 0:
                    vi += 1
                    print(f'você jogou {lp} e o computador {pc}. Total de {lp + pc} deu PAR')
                    print('O jogador ganhou.... :)')
                    retu = str(input('Jogar novamente? ')).upper()
                    if retu == 'N':
                        if vi == 1:
                            print('Você conseguiu ganha apenas uma vez')
                        if vi > 1:
                            print(f'Você conseguiu {vi} vitorias consecutivas')
                        break
                else:
                    print(f'você jogou {lp} e o computador {pc}. Total de {lp + pc} deu IMPAR')
                    print('O jogador perdeu.... :( \n'
                          'assim acabou com suas vidas..\n')
                    if vi == 1:
                        print('Você conseguiu ganha apenas uma vez')
                    if vi > 1:
                        print(f'Você conseguiu {vi} vitorias consecutivas')
                    break
            else:
                print('COMANDO IVALIDO, TENTE NOVAMENTE')
        a = str(input('Deseja continuar jogano esse jogo? (y/n)')).upper()
        if a == 'N':
            break

    while cd == 4:
        def on_grid_random():
            x = random.randint(0, 59)
            y = random.randint(0, 59)
            return (x * 10, y * 10)


        def collision(c1, c2):
            return (c1[0] == c2[0]) and (c1[1] == c2[1])


        # Macro definition for snake movement.
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Snake')

        snake = [(200, 200), (210, 200), (220, 200)]
        snake_skin = pygame.Surface((10, 10))
        snake_skin.fill((255, 255, 255))  # White

        apple_pos = on_grid_random()
        apple = pygame.Surface((10, 10))
        apple.fill((255, 0, 0))

        my_direction = LEFT

        clock = pygame.time.Clock()

        font = pygame.font.Font('freesansbold.ttf', 18)
        score = 0

        game_over = False
        while not game_over:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_UP and my_direction != DOWN:
                        my_direction = UP
                    if event.key == K_DOWN and my_direction != UP:
                        my_direction = DOWN
                    if event.key == K_LEFT and my_direction != RIGHT:
                        my_direction = LEFT
                    if event.key == K_RIGHT and my_direction != LEFT:
                        my_direction = RIGHT

            if collision(snake[0], apple_pos):
                apple_pos = on_grid_random()
                snake.append((0, 0))
                score = score + 1

            # Check if snake collided with boundaries
            if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
                game_over = True
                break

            # Check if the snake has hit itself
            for i in range(1, len(snake) - 1):
                if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                    game_over = True
                    break

            if game_over:
                break

            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i - 1][0], snake[i - 1][1])

            # Actually make the snake move.
            if my_direction == UP:
                snake[0] = (snake[0][0], snake[0][1] - 10)
            if my_direction == DOWN:
                snake[0] = (snake[0][0], snake[0][1] + 10)
            if my_direction == RIGHT:
                snake[0] = (snake[0][0] + 10, snake[0][1])
            if my_direction == LEFT:
                snake[0] = (snake[0][0] - 10, snake[0][1])

            screen.fill((0, 0, 0))
            screen.blit(apple, apple_pos)

            for x in range(0, 600, 10):  # Draw vertical lines
                pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
            for y in range(0, 600, 10):  # Draw vertical lines
                pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

            score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
            score_rect = score_font.get_rect()
            score_rect.topleft = (600 - 120, 10)
            screen.blit(score_font, score_rect)

            for pos in snake:
                screen.blit(snake_skin, pos)

            pygame.display.update()

        while True:
            game_over_font = pygame.font.Font('freesansbold.ttf', 75)
            game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
            game_over_rect = game_over_screen.get_rect()
            game_over_rect.midtop = (600 / 2, 10)
            screen.blit(game_over_screen, game_over_rect)
            pygame.display.update()
            pygame.time.wait(500)
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()

    while cd == 5:
        print(f'Ao total você teve,'
              f'{vitorias}° vitorias,\n'
              f'{derrotas}° derrotas,\n'
              f'e {empate}° empates')

    while cd == 6:
        a = 1
    while cd == 7:
        break