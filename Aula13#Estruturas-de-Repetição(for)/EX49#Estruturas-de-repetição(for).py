#Estruturas de repetição(for).

#49 - Refaça o exercício 009, mostrando a tabuada de um usuário, utilizando o laço for.

n=int(input('Digite um numero: '))
for c in range(0, 10+1):
    print(f'{n} x {c} = {n*c}')

    '''m = n * c
    print('{} x {} = {}'.format(n,c,m))'''
