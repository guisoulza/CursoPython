#Tipos primitivos e saída de Dados.

#04 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

n=input('Digite algo: ')
print('É numérico? ', n.isnumeric())                    #Nesta linha o .isnumeric() vai mostrar se o dado é um número.
print('Tem letras? ', n.isalpha())                      #Nesta linha o .isalpha() vai mostrar se o dado possui letras.
print('Tem letras ou numéros? ', n.isalnum())           #Nesta linha o .isalnum() vai mostrar se o dado tem números ou letras.
print('Está em maiusculo? ', n.isupper())               #Nesta linha o .isupper() vai mostrar se o dado está em maiúsculo.
print('Está em minusculo? ', n.islower())               #Nesta linha o .islower() vai mostrar se o dado está em minúsculo.
print('É um titulo? ', n.istitle())                     #Nesta linha o .istitle() vai mostrar se o dado tem a sua primeira letra maiúscula para ser considerado como titúlo.
print('É um espaço? ', n.isspace())                     #Nesta linha o .isspace() vai mostrar se o dado é um espaço.
print('Forma correta: ', n.capitalize())                #Nesta linha o .capitalize() vai mostrar o dado com a primeira letra maiúscula.
print('Seu tipo é: ', type(n))                          #Nesta linha o type() vai mostrar o tipo de dado que o usuário digitou.
