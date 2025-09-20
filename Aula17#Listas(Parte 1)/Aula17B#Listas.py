valores = list()
valores.append(1)
valores.append(2)
valores.append(3)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}!')

