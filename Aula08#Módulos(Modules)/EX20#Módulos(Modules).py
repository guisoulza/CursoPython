# Módulos(Modules).

# 20 - O mesmo professor do exercício anterior quer sortear a ordem dos trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.
# 20 - The same teacher from the previous exercise wants to randomly sort the order of student presentations.
# Create a program that reads the names of the four students and shows the randomized order.

from random import shuffle
"""import random"""

a1=str(input('Digite o nome do 1º aluno: '))
a2=str(input('Digite o nome do 2º aluno: '))
a3=str(input('Digite o nome do 3º aluno: '))
a4=str(input('Digite o nome do 4º aluno: '))
aq=[a1,a2,a3,a4]
random.shuffle(aq)
# shuffle() Embaralha os elementos de uma lista no próprio lugar.
# shuffle() shuffles the elements of a list in place.
"""
shuffle(aq)
sorteio=sorted(aq)
"""
print('A ordem é {}'.format(aq))