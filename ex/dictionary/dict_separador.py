dados_p = dict()
dados_t = list()
perg = 'sim'
total = 0
ida = 0
fem = str()
while True:
    if perg in 'simSIM':
        dados_p['nome'] = str(input('Nome: '))
        dados_p['sexo'] = str(input('Sexo: [M/F]')).upper()
        if dados_p['sexo'] == 'F':
            fem = fem + dados_p['sexo'] + ','
        dados_p['idade'] = int(input('Idade: '))
        dados_t.append(dados_p.copy())
        total += 1
        ida += dados_p['idade']
        perg = str(input('Quer continuar? [S/N] '))
    if perg in 'naonãoNAONÃo':
        ida = ida/2
        break
print('-=' * 30)
print(f'- O grupo tem {total} pessoas.\n'
      f'- A média de idade é de {ida}.'
      f'- As mulheres cadastradas foram: {fem}'
      f'- Lista das pessoas que estão acima da média:'
      )
