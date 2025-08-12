#Módulos.

import random
#from random import choice
a1=str(input('Digite o nome do 1º aluno: '))
a2=str(input('Digite o nome do 2º aluno: '))
a3=str(input('Digite o nome do 3º aluno: '))
a4=str(input('Digite o nome do 4º aluno: '))
aq=[a1,a2,a3,a4]
sorteio=random.choice(aq)
#sorteio=choice(aq)
print('Quem vai apagar a lousa é o {}'.format(sorteio))