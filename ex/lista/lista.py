lista = list()
group = list()
fat = lean = 0
while True:
    name = str(input('Qual o nome da pessoa? '))
    kg = float(input('Qual o peso da pessoa? '))
    print('')
    lista.append(name)
    lista.append(kg)
    while True:
        r = str(input('Deseja continuar?(y/n) '))
        if r in 'Yy':
            break
        elif r in 'Nn':
            break
    if fat == 0:
        fat = lean = kg#kg
    else:
        if kg > fat:
            fat = kg
        if kg < lean:
            lean = kg
    group.append(lista[:])
    lista.clear()
    print('')
    if r in 'Nn':
        break
print('-=' * 30)
print(f'O total da pesquisa foi de {len(group)} pessoas.\n')
print(f'com a pessoa mais gorda pesando {fat}KG, com nome de ', end='')
for c in group:
    if c[1] == fat:
        print(c[0] , end=',')
print(f'e a mais magra com {lean}KG, com nome de ', end='')
for c in group:
    if c[1] == lean:
        print(c[0], end=',')
