# Operadores Aritiméticos (Arithmetic Operators).

# 07 - Desenvolva um programa que leia 2 notas de aluno e calcule e mostre a média.
# 07 - Develop a program that reads 2 students grades and calculates and shows the average.

n1=float(input('Digite a nota da prova: '))
n2=float(input('Digite a nota do trabalho: '))
m=(n1+n2)/2
print('A média do aluno é {:.1f}'.format(m))