#Condições Simples e Compostas.

a = float(input('Digite a medida: '))
b = float(input('Digite a medida: '))
c = float(input('Digite a medida: '))
if a < b + c and b < a + c and c < a + b:
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