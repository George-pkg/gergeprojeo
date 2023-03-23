everybody = list()
sn = 'y'
while True:
    if sn in 'Yy':
        nome = str(input('NOME: '))
        nota1 = float(input(f'Nota 1: '))
        nota2 = float(input(f'Nota 2: '))
        media = nota1 + nota2 / 2
        everybody.append([nome, [nota1, nota2], media])
    sn = str(input('Quer continuar? (y/n) '))
    if sn in 'Nn':
        break
print('-='*15)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(everybody):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*30)
while True:
    perg = int(input('Deseja ver as notas de qual aluno? (999 interrompe): '))
    if perg == 999:
        print('FINALIZANDO...')
        break
    if perg <= len(everybody) - 1:
        print(f'Notas de {everybody[perg][0]} são {everybody[perg][1]}')
print('<<< VOLTE SEMPRE >>>')