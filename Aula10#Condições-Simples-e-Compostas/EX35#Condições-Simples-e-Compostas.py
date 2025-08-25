#Condições Simples e Compostas.

#35 - Desenvolva um programa que leia o comprimento de 3 rotas e diga se podem ou não formar um triângulo.

a = float(input('Digite a medida: '))
b = float(input('Digite a medida: '))
c = float(input('Digite a medida: '))
if a < b + c and b < a + c and c < a + b:                               #Esse if verifica se três comprimentos podem formar um triângulo.
    print('\033[4;32mOs segmentos formam um triangulo\033[m')
else:
    print('\033[4;31mOs segmentos não formam um triangulo\033[m')


'''
if a + b > c:
    if a + c > b:
        if b + c > a:
            print('Dá pra formar um triangulo!')
        else:
            print('Não dá pra formar um triangulo!')
    else:
        print('Não dá pra formar um triangulo!')
else:
    print('Não dá pra formar um triangulo!')
'''