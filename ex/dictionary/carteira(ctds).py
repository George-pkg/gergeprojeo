dice = dict()
dice['nome'] = str(input('Nome: '))
date = int(input('Data de nascimento: '))
dice['nascimento'] = 2022 - date
dice['ctps'] = int(input('Carteira e Trabalho(0 não tem): '))
if dice['ctps'] != 0:
    dice['contratação'] = int(input('Ano de Contratação: '))
    dice['salário'] = int(input('Salário: R$ '))
    print('-=' * 30)
    contrat = 2022 - dice['contratação']
    while True:
        if contrat < 35:
            apo = (2022 - date) + 1
            contrat += 1
        if contrat >= 35:
            break
    dice['aposentadoria'] = apo
    print(dice)
    for i, q in enumerate(dice):
        print(f'{q} tem o valor {dice[i]}.')
else:
    print('-=' * 30)
    print(dice)
