# Operadores Aritiméticos (Arithmetic Operators).

# 13 - Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# 13 - Make a program that reads the salary of one employee and show the new salary, with 15% raise.

s=float(input('Salário: R$'))
#b=s/100*15
#a=s+b
a=s+(s*15/100)
print('O novo salário é de: R${}'.format(a))