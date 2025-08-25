#Condições Simples e Compostas.

#29 - Escreva um programa que leia a velocidade de um carro. Se passar de 80km/h mostre que foi multado. A multa vai custar R$7,00 por cada km/h acima do limite.

v = int(input('Qual a velocidade do carro?\n'))
m = float((v-80) * 7)
if v > 80:
    print('\033[4;31mVocê foi multado\033[m ')
    print('\033[4;31mO valor da multa é R${:.2f}\033[m'.format(m))
else:
    print('\033[4;32mVocê está dentro do limite\033[m')
