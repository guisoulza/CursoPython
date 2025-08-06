#Estruturas de repetição(for).

'''
for c in range(0, 6):
    print('OI')
print('Fim')
for c in range(6, 0, -1):
    print(c)
print('Fim')
for c in range(0, 7, 2):
    print(c)
print('Fim')
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')
'''
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores é {}'.format(s))