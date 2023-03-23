c = q = 0
while True:
    if c == 0:
        n = int(input('Digite um número: '))
        if n == 999:
            break
    else:
        n = int(input('Digite outro número: '))
        if n == 999:
            break
    q += n
    c += 1
print(f'Você digitou {c} números e a soma deles é {q}')
