#Condições Aninhadas.

#37 - Escreva um programa que leia um número inteiro qualquer  e peça para o usuário escolher qual será a base de conversão:

# 1 para binário;
# 2 para octal;
# 3 para hexadecimal.

num = int(input('Qual o numero?\n'))
print('1 para binario\n2 para octal\n3 para hexadecimal')
escolhanum = int(input('Qual a base de conversão você deseja?\n'))
if escolhanum == 1:
    print(bin(num)[2:])                         #bin() transforma o número em binário.
elif escolhanum == 2:
    print(oct(num)[2:])                         #oct() transforma o número em octal.
elif escolhanum == 3:
    print(hex(num)[2:])                         #hex() transforma o número em hexa decimal.
else:
    print('\033[31mErro!\033[m')