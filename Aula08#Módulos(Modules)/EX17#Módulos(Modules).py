# Módulos(Modules).

# 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
# 17 - Create a program that reads the length of the opposite and adjacent sides of a right triangle, calculates, and
# shows the length of the hypotenuse.

import math
# from math import hypot
# A biblioteca math traz várias funções e constantes úteis para cálculos que vão além do básico.
# The math library provides many useful functions and constants for calculations beyond the basics.
c1=float(input('Digite o cateto adjacente: '))
c2=float(input('Digite o cateto oposto: '))
h1=math.hypot(c1,c2)
# h1=hypot(c1,c2)
# hypot() é usada para calcular a hipotenusa de um triângulo retângulo usando o Teorema de Pitágoras.
#hypot() is used to calculate the hypotenuse of a right triangle using the Pythagorean theorem.
print('A hipotenusa é {:.2f}'.format(h1))

"""
h1=(c1**2+c2**2)**(1/2)
print('A hipotenusa é {:.2f}'.format(h1))
"""