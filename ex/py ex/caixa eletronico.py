print('=' * 30)
print('{:^30}'.format('BANCO GERGES'))
print('=' * 30)
nota = int(input('Qual valor você que sacar? R$'))
total = nota
din = 50
totdin = 0
while True:
    if total >= din:
        total -= din
        totdin += 1
    else:
        print(f'Total de {totdin} cédulas de R${din}')
        if din == 50:
            din = 20
        elif din == 20:
            din = 10
        elif din == 10:
            din = 1
        totdin = 0
        if total == 0:
            break