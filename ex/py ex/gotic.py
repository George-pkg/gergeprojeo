nome = str(input('Quem está no pc? ')).lower()
if nome == 'george' or nome == 'gerge':
    bem_star = str(input('Bom dia meu criador, como você está? ')).lower()
    if bem_star == 'nao' or bem_star == 'não':
        perg = str(input('já que você não está bem, vamos jogar um jogo? (y/n) ')).upper()
    while True:
        if perg == 'Y':
            jg = int(input('Ebaaaa, vamos jogar qual jogo dessa vez?\n'
                           '1 ======> (impar ou par) '))
            if jg == 1:
                import random
                import time

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
        if perg == 'N':
            print('que pena, eu realmente queria jogar algo contigo.\n'
                  'Quem sabe da proxima vez...')
            break
else:
    bem_star = str(input(f'Bom dia {nome}, como você está?')).lowe()
    if bem_star == 'nao' or bem_star == 'não':
        perg = str(input('posso tentar te alegrar, vamos jogar um jogo? (y/n) ')).upper()

