a = [2, 3, 4, 7]
"""
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
"""

#A partir do momento que é atribuido uma lista a outra elas tem um vinculo que quando uma é modificada a outra muda junto

b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Utilizando o fatiamento o valor atribuido a variavel b será um copia da lista a