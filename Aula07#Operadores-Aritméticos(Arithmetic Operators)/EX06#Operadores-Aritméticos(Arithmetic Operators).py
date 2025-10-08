# Operadores Aritiméticos (Arithmetic Operators).

# 06 - Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
# 06 - Create an algorithm that reads a number and shows its double, triple, and square root.

n1=int(input('Digite um número: '))
d=n1*2
t=n1*3
r=n1**(1/2)
print('O dobro de {} é {} \nO triplo é {} \nE sua raiz quadrada é {:.3f}'.format(n1, d, t, r))