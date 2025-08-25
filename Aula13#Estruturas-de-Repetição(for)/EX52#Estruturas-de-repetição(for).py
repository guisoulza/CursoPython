#Estruturas de repetição(for).

#52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

p = int(input('Digite um valor: '))
tot = 0
for i in range(1, p+1):
    if p % i == 0:                                          #Condição para se o resto da divisão de p com i é igual a 0.
        print(f'\033[32m', end='')
        tot += 1
    else:
        print(f'\033[31m', end='')
    print(f'{i}', end=' ')
print(f'\nO número {p} foi divisivel {tot} vez(es)')
if tot == 2:                                                #Condição para se o total de vezes dividida for 2.
    print(f'\n{p} é primo')                                 #Se a condição for verdadeira vai mostrar se ele é um número primo.
else:
    print(f'\n{p} não é primo')