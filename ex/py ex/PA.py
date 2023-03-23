num = int(input('Dígite um numero para saber a PA(Pogreção arítimetica) dele: '))
pa = int(input('Dígite uma codinção da PA:'))
lim = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while lim != total:
        print(f'{num}', end='')
        print(', ' if lim < total else '.', end='')
        lim += 1
        num += pa
    mais = int(input('\nVocê dejesa ver mais quantos termos? '))
print('FIM')
