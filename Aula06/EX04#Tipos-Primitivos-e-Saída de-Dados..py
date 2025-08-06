#Tipos primitivos e saída de Dados.

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
