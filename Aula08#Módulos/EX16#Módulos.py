#Módulos.

#16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc                              #O metodo trunc() serve para truncar um número, ou seja, ele remove a parte decimal e retorna apenas a parte inteira, sem arredondar.
#import math
numero = float(input('Digite um valor real: '))
print('O {} tem parte inteira {}'.format(numero, trunc(numero)))
#print('O {} tem parte inteira {}'.format(numero, math.trunc(numero)))
numero = float(input('Digite um valor real: '))
print('O {} tem parte inteira {}'.format(numero, int(numero)))
