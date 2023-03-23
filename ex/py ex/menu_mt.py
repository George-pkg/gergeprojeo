play = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while play != 5:
    print('')
    play = int(input('\033[34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
                     '= OQUE DESEJA FAZER COM OS NÚMEROS: =\n'
                     '=                                   =\n'
                     '=[1]SOMAR                           =\n'
                     '=[2]MUTIPLICAR                      =\n'
                     '=[3]MAIOR                           =\n'
                     '=[4]NOVOS NÚMEROS                   =\n'
                     '=[5]SAIR DO PROGRAMA                =\n'
                     '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m'))
    print('')
    if play == 1:
        print('A soma dos números digitados é {}'.format(n1 + n2))
    elif play == 2:
        print('A mutiplicação dos números escolidos é {}'.format(n1 * n2))
    elif play == 3:
        if n1 > n2:
            print('O número {} é maior que o {}.'.format(n1, n2))
        elif n1 < n2:
            print('O número {} é maior que o {}.'.format(n2, n1))
        else:
            print('os números tem o mesmo valores.')
    elif play == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    if play == 5:
        print('Obrigado por experimentar meu programa!! ')
