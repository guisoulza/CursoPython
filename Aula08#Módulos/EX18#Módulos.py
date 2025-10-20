# Módulos(Modules).

# 18 - faça um programa que leia um ângulo qualquer e mostre seu seno, cosseno e tangente desse angulo.
# 18 - Create a program that reads any angle and shows its sine, cosine, and tangent.


"""import math"""
from math import radians, sin, cos, tan

a=int(input('Digite o angulo: '))
"""s=math.sin(math.radians(a))"""            # radians() converte graus para radiano.
"""c=math.cos(math.radians(a))"""            # radians() function converts degrees to radians.
"""t=math.tan(math.radians(a))"""
s=sin(radians(a))                            # sin() calcula o seno(sin() calculates the sine).
c=cos(radians(a))                            # cos() calcula o cosseno(cos() calculates the cosine).
t=tan(radians(a))                            # tan() calcula o tangente(tan() calculates the tangent).
print('O valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(s, c, t))