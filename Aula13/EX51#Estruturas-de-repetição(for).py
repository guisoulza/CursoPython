#Estruturas de repetição(for).

n = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
d = n + (10 - 1) * r
print('Progressão Aritmética: ', end='')
for i in range(n, d + r, r):
    print(i, end=' ')