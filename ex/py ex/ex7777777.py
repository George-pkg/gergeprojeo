num = list()
for cont in range(0, 5):
    num.append(int(input('Digite um valor:')))
print(20* '=-')
print(f'Os números que você digitou foram {num}')
maior = menor = 0
print(f'Você digitou os valores {num}')
print(f'O maior número digitado é: {max(num)} na posição {num.index(max(num))+ 1}')
print(f'O menor número digitado é: {min(num)} na posição {num.index(min(num))+ 1}')
