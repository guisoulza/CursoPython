#Operadores Aritméticos.

#13 - Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s=float(input('Salário: R$'))
#b=s/100*15
#a=s+b
a=s+(s*15/100)
print('O novo salário é de: R${}'.format(a))