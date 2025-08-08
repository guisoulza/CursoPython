n = int(input('Digite um número: '))
original = n
f = 1
while n > 0:
    f = f * n
    n = n - 1
print(f'O fatorial de {original} é igual a {f}')
