#Módulos.

import math
#from math import hypot

c1=float(input('Digite o cateto adjacente: '))
c2=float(input('Digite o cateto oposto: '))
h1=math.hypot(c1,c2)
#h1=hypot(c1,c2)
print('A hipotenusa é {:.2f}'.format(h1))

"""
h1=(c1**2+c2**2)**(1/2)
print('A hipotenusa é {:.2f}'.format(h1))
"""