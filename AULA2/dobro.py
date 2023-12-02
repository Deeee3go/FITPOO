def dobrar(x):
    return x * 2


def triplicar(x):
    triplo = x * 3
    return triplo


n1 = float(input('Digite um número: '))
dobro = dobrar(n1)
print('O dobro é ', {dobro})
print(f'O triplo é {triplicar(n1)}')
