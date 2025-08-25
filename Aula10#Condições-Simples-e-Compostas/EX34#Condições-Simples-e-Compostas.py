#Condições Simples e Compostas.

#34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%. Para inferiores ou iguais o aumento é de 15%.

s = float(input('Digite o salário: '))
if s <= 1250:
    print('O valor do aumento é R${:.2f}'.format(s / 100 * 10))
    print('O novo salário é de R${:.2f}'.format(s / 100 * 10 + s))
else:
    print('O valor do aumento é R${:.2f}'.format(s / 100 * 15))
    print('O novo salário é de R${:.2f}'.format(s / 100 * 15 + s))