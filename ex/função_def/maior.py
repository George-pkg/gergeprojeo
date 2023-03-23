import time, random


def maior(a):
    m = q = 0
    for nu in a:
        if q == 0:
            m = nu
        else:
            if nu > m:
                m = nu
        q += 1
    return m


def aleatorio(quant, max=9):
    z = list()
    for quant in range(0, quant):
        z.append(random.randint(1, max))
    return z


def pares(numeros):
    c = list()
    for i, n in enumerate(numeros):
        if n % 2 == 0:
            c[m].append(c)
    return c


a1 = int(input('Digite quantos números quer sortear: '))
m2 = int(input('Dígite qual o limite do sorteador: '))
num = aleatorio(a1, m2)
print(num)
print('-=' * 20)
print(f'O maior número sorteado foi {maior(num)}')
print('-=' * 20)
print(f'Os valores pares são: {pares(num)}')
