import time


def passos(inicio, final, passos):
    i = inicio
    f = final
    p = passos
    if p == 0:
        p = 1
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        while True:
            if i <= f:
                print(f'{i}, ', end='')
                time.sleep(0.5)
                i += p
            else:
                print('FIM!!')
                break
    if i > f:
        while True:
            if i >= f:
                print(f'{i}, ', end='')
                time.sleep(0.5)
                i -= p
            else:
                print('FIM!!')
                break
    print('-=' * 30)


a = int(input('Inicío: '))
b = int(input('Final: '))
pas = int(input('Passos: '))
passos(a, b, pas)
