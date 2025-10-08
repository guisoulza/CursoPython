# Operadores Aritiméticos (Arithmetic Operators).

# 11 - Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la sabendo que cada litros de tinta pinta uma área de 2m².
# 11 - Write a program that reads the height and width of a wall in meters, calculates its area, and the amount of paint
# needed to cover it, knowing that each liter of paint covers 2 m².

a=float(input('Digite a altura: '))
l=float(input('Digite a largura: '))
m=a*l
t=m/2
print('\033[7mSua parede tem a dimenção de {}x{} e sua area é de {}m²\033[m'.format(a,l,m))
print('\033[7mVai precisar de {} litros de tinta para pintar {}m² da parede\033[m'.format(t,m))