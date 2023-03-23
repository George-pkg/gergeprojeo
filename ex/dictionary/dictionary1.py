student = dict()
school = list()
student['nome'] = str(input('Qual o nome do aluno? '))
student['nota'] = int(input(f'Qual a nota média de {student["nome"]} ? '))
if student['nota'] >= 5:
    student['média'] = 'Aprovado'
if student['nota'] <= 5:
    student['média'] = 'Reprovado'
print(f'O nome do aluno é {student["nome"]},\n'
      f'A sua nota média é {student["nota"]},\n'
      f'E sua situação é {student["média"]}')
