#Módulos.

#import math
from math import radians, sin, cos, tan

a=int(input('Digite o angulo: '))
#s=math.sin(math.radians(a))
#c=math.cos(math.radians(a))
#t=math.tan(math.radians(a))
s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))
print('O valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(s, c, t))