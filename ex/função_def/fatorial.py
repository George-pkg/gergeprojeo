def fatorial(num, show=False):
    for n in range(num, 0, -1):
        if show == True:
            num *= n
            print(f'{n} x ', end='')
        if show == False:
            num *= n
            return num
    print(num)


print('-=' * 20)
a = int(input('Escreva um número para ter o fatorial: '))
ver = input('Quer ver a conta? ')
print('-=' * 20)
fatorial(a, show=True)
