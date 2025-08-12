#Tipos primitivos e saída de Dados.

#04 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

n=input('Digite algo: ')
print('É numérico? ', n.isnumeric())
print('Tem letras? ', n.isalpha())
print('Tem letras ou numéros? ', n.isalnum())
print('Está em maiusculo? ', n.isupper())
print('Está em minusculo? ', n.islower())
print('É um titulo? ', n.istitle())
print('É um espaço? ', n.isspace())
print('Forma correta: ', n.capitalize())
print('Seu tipo é: ', type(n))
