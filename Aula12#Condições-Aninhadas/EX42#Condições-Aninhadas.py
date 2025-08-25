#Condições Aninhadas.

#42 - Refaça o Exercício 035 dos triângulos, acrescentando o tipo de triângulo será formado:

#Equilátero: Lados iguais;
#Isósceles: 2 lados iguais;
#Escaleno: Lados diferentes.

a = float(input('Digite a medida: '))
b = float(input('Digite a medida: '))
c = float(input('Digite a medida: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[4;32mOs segmentos formam um triangulo\033[m')
    if a == b == c:
        print('Triangulo Equilatero')
    elif a == b or a == c or b == c:
        print('Triangulo Isosceles')
    elif a != b or a != c or b != c:
        print('Triangulo Escaleno')
else:
    print('\033[4;31mOs segmentos não formam um triangulo\033[m')