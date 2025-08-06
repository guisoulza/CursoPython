#Estruturas de repetição(for).

p = int(input('Digite um valor: '))
tot = 0
for i in range(1, p+1):
    if p % i == 0:
        print(f'\033[32m', end='')
        tot += 1
    else:
        print(f'\033[31m', end='')
    print(f'{i}', end=' ')
print(f'\nO número {p} foi divisivel {tot} vez(es)')
if tot == 2:
    print(f'\n{p} é primo')
else:
    print(f'\n{p} não é primo')