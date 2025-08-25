#Estruturas de repetição(while).

#60 - Faça um programa que leia um número qualquer e mostre seu fatorial.

n = int(input('Digite um número: '))
original = n
f = 1
while n > 0:                                                            #Nesta linha o loop vai funcionar até a variável (n) chegar a 0
    f = f * n                                                           #O fatorial será feito nessa operação
    n = n - 1                                                           #Faz a subtração com - 1 para realizar o cálculo do proximo número
print(f'O fatorial de {original} é igual a {f}')


#Correção

"""
from math import factorial                                              #Forma de fazer com 4 linhas mas sem while
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é igual a {f}')


n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:                                                            #Nesta linha o loop vai funcionar até a variável contadora (c) chegar a 0
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')                            #Essa condição dentro do print vai adicionar o carácter "x" enquanto a variável contadora (c) for maior que 1 o carácter "=" no último número do cálculo
    f *= c                                                              #O fatorial será feito nessa operação
    c -= 1                                                              #Faz a subtração com - 1 para realizar o cálculo do proximo número
print(f'{f}')

#Desta forma que o professor fez ficou mais simples e completa
"""
