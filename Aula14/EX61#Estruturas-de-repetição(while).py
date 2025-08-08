#Estruturas de repetição(while).

n = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
termo = n
cont = 1
print('Progressão Aritmética: ', end='')
while cont <= 10:
    print(termo, end=' ')
    termo += r
    cont += 1