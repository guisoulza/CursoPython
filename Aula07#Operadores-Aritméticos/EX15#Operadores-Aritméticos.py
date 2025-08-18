#Operadores Aritméticos.

#15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado

km=float(input('Km percorridos: '))
d=int(input('Dias percorridos: '))
p=d*60+km*0.15
print('Andou {}km por {} dias'.format(km,d))
print('Valor total a pagar: R${:.2f}'.format(p))