#Tuplas

#74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
print(f'Tupla aleatória: {tupla}')
print(f'O maior valor é: {max(tupla)}')
print(f'O menor valor é: {min(tupla)}')

#max() e min() facilitam demais a minha vida.