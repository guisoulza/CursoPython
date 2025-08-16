"""
cont = 1
while True:                                        #Utilizando esse loop a execução se tornará infinita
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

n = cont = 0
while n != 999:                                    #Loop  com uma condição de parada
    n = int(input('Digite um número: '))
    cont += 1

n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999                                           #Nesta linha e feito a subtração do valor 999 da condição de parada para realizar a soma correta, mas não é recomendável
print(f'A soma vale {s}')
"""

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:                                   #Nesta condição a execução vai desconsiderar o 999 para realizar a interrupção do programa com o break
        break
    s += n
print(f'A soma vale {s}')