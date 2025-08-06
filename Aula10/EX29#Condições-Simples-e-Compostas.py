#Condições Simples e Compostas.

v = int(input('Qual a velocidade do carro?\n'))
m = float((v-80) * 7)
if v > 80:
    print('\033[4;31mVocê foi multado\033[m ')
    print('\033[4;31mO valor da multa é R${:.2f}\033[m'.format(m))
else:
    print('\033[4;32mVocê está dentro do limite\033[m')
