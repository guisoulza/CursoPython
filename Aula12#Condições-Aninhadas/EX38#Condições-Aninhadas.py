#Condições Aninhadas.

#38 - Escreva um programa que leia dois números inteiros e compare-os mostrando na tela um mensagem:

#O primeiro valor é maior;
#O segundo valor é menor;
#Os 2 valores são iguais.

num1 = int(input('Escolha o valor: '))
num2 = int(input('Escolha o valor: '))
if num1 > num2:
    print('O valor {} é maior que o valor {}'.format(num1, num2))
elif num2 > num1:
    print('O valor {} é maior que o valor {}'.format(num2, num1))
else:
    print('Os valores são iguais')