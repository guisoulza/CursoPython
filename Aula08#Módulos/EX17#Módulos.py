#Módulos.

#17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math                                 #A biblioteca math traz várias funções e constantes úteis para cálculos que vão além do básico.
#from math import hypot

c1=float(input('Digite o cateto adjacente: '))
c2=float(input('Digite o cateto oposto: '))
h1=math.hypot(c1,c2)            #hypot() é usada para calcular a hipotenusa de um triângulo retângulo usando o Teorema de Pitágoras.
#h1=hypot(c1,c2)
print('A hipotenusa é {:.2f}'.format(h1))

"""
h1=(c1**2+c2**2)**(1/2)
print('A hipotenusa é {:.2f}'.format(h1))
"""