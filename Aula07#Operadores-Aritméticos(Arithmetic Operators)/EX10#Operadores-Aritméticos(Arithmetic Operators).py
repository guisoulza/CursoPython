# Operadores Aritiméticos (Arithmetic Operators).

# 10 - Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos dólares ela pode comprar.
# 10 - Create a program that reads how much money is in the wallet and shows how many dollars can be bought.

r=float(input('Quantos reais você tem? R$'))
d=r/3.27
print('Você consegue comprar ${:.2f}.'.format(d))
