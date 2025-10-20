# Módulos(Modules).

# 16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# 16 - Create a program that reads any real number from the keyboard and shows its integer part on the screen.

from math import trunc
# O metodo trunc() serve para truncar um número, ou seja, ele remove a parte decimal e retorna apenas a parte inteira,
# sem arredondar.
# The trunc() method is used to truncate a number, that is, it removes the decimal part and returns only the integer
# part, without rounding.
numero = float(input('Digite um valor real: '))
print('O {} tem parte inteira {}'.format(numero, trunc(numero)))
numero = float(input('Digite um valor real: '))
print('O {} tem parte inteira {}'.format(numero, int(numero)))
