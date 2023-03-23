numeros = []
for c in range(0, 5):
    n = int(input('Digite um número inteiro qualquer: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado a posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'a lista coreta é {numeros}')

#=============================================================================================

numeros = list()
while True:
    n = int(input('Digite um valor para ser adicionado na sua lista: '))
    if n not in numeros:
        numeros.append(n)
    while True:
        s = str(input('Deseja continuar a colocar números na lista?(y/n) '))
        if s in 'Yy' or s in 'Nn':
            break
    if s in 'Nn':
        break
print()
numeros.sort(reverse=True)
print(f'Você digitou {len(numeros)} números...\n'
      f'eles em ordem decrecente é {numeros}')

#================================================================================================

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
