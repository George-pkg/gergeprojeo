def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m²')


print('')
print('  Controle de Terrenos')
print('----------------------')
lc = float(input('LARGURA (m): '))
cc = float(input('COMPRIMENTO (m): '))
area(lc, cc)
