# Manipulando Cadeias de Texto (Manipulating Text Strings).

# 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela sua milhar, centena, dezena e unidade.

# 23 - Create a program that reads a number from 0 to 9999 and displays its thousands, hundreds, tens, and units.

num=int(input("Digite um numero: "))
u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))
