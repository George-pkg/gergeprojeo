print(24* '\033[33m=')
print('SEQUÊNCIA DE FIBONACCI')
print(24* '=')
lim = int(input('\033[mQuantos termos você quer mostrar? '))
f1 = 0
f2 = 1
print(f'{f1} -> ', end='')
num = 0
if lim > 0:
    while num != lim:
        num += 1
        f3 = f1 + f2
        print(f'{f3} -> ', end='')
        f1 = f2
        f2 = f3
else:
    lim = int(input('Por favor digite um números reais. '))
print('FIM')