def la(texto):
    tam = len(texto) + 4
    print('-' * tam)
    print(f'    {texto}')
    print('-' * tam)


la(str(input('Qual frase você quer destacar? ')))