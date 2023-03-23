v = 1
while True:
    print('=-=-=-=--=--=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    v = int(input('QUER VER A TABUAA DE QUAL VALOR?: '))
    print('=-=-=-=--=--=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    if v > 0:
        for vz in range(1, 11):
            print(f'{v} x {vz} = {v * vz}')
    else:
        print('')
        print('Obrigado por usar meu programa!')
        break