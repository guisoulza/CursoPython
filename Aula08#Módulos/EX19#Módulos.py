#Módulos.

#19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

import random                                               #O módulo random serve para gerar números aleatórios, escolher itens aleatórios e até embaralhar sequências.
#from random import choice
a1=str(input('Digite o nome do 1º aluno: '))
a2=str(input('Digite o nome do 2º aluno: '))
a3=str(input('Digite o nome do 3º aluno: '))
a4=str(input('Digite o nome do 4º aluno: '))
aq=[a1,a2,a3,a4]
sorteio=random.choice(aq)                                   #choice() escolhe aleatoriamente um elemento de uma sequência
#sorteio=choice(aq)
print('Quem vai apagar a lousa é o {}'.format(sorteio))