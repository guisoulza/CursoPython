#Tuplas

#74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
print(f'Tupla aleatória: {tupla}')                              #Eu poderia usar o join() mas ele só funciona com strings
print(f'O maior valor é: {max(tupla)}')
print(f'O menor valor é: {min(tupla)}')

#max() e min() facilitam demais a minha vida.

#Correção

"""
from random import randint

tupla = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
print(f'Os números sorteados foram:', end=' ')
for n in tupla:                                              #Não esquecer dessa forma de realizar a ordem de números sem aparecer os parentêses
    print(f'{n}', end=' ')
print(f'O maior valor é: {max(tupla)}')
print(f'O menor valor é: {min(tupla)}')
"""