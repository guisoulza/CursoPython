#Módulos.

from math import sqrt,ceil,floor                    #sqrt calcula a raiz quadrada de num
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é igual a {}'.format(num, math.floor(raiz)))

#ceil: arredonda sempre para cima.
#floor: arredonda sempre para baixo.