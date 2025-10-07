# Tipos Primitivos e Saída de Dados(Primitive Types and Data Output).

# 04 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possiveis sobre ele.
# 04 - Write a program that reads input from the keyboard and displays its primitive type and all possible information
# about it.

n=input('Digite algo: ')
print('É numérico? ', n.isnumeric())                     # Nesta linha o .isnumeric() vai mostrar se o dado é um número.
print('Tem letras? ', n.isalpha())                       # Nesta linha o .isalpha() vai mostrar se o dado possui letras.
print('Tem letras ou numéros? ', n.isalnum())    # Nesta linha o .isalnum() vai mostrar se o dado tem números ou letras.
print('Está em maiusculo? ', n.isupper())            # Nesta linha o .isupper() vai mostrar se o dado está em maiúsculo.
print('Está em minusculo? ', n.islower())            # Nesta linha o .islower() vai mostrar se o dado está em minúsculo.
print('É um titulo? ', n.istitle()) # Nesta linha o .istitle() vai mostrar se o dado tem a sua primeira letra maiúscula.
print('É um espaço? ', n.isspace())                        # Nesta linha o .isspace() vai mostrar se o dado é um espaço.
print('Forma correta: ', n.capitalize())# Nesta linha o .capitalize() vai mostrar o dado com a primeira letra maiúscula.
print('Seu tipo é: ', type(n))                  # Nesta linha o type() vai mostrar o tipo de dado que o usuário digitou.

# In line 9, isnumeric() will show if the data is a number.
# In line 10, isalpha() will show if the data contains letters.
# In line 11, isalnum() will show if the data has letters or numbers.
# In line 12, isupper() will show if the data is in uppercase.
# In line 13, islower() will show if the data is in lowercase.
# In line 14, istitle() will show if the data has its first letter capitalized.
# In line 15, isspace() will show if the data is a space.
# In line 16, capitalize() will show the data with the first letter capitalized.
# In line 17, type() will show the type of data the user entered.