#Tuplas

"""
lanche = 'hamburguer'                                   #Dessa forma vai eliminar uma variável para dar espaço para outra.
lanche = 'suco'

print(lanche)
"""

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batata frita')       #Tuplas são imutáveis.
"""
lanche[1] = 'Refrigerante'                              #Vai dar erro de atribuição porque tuplas são imutáveis.
"""
print(lanche)
print(lanche[3])
print(lanche[-3])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])
print(len(lanche))

"""
for comida in lanche:
    print(f'Eu vou comer {comida}')
"""

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')


#Ambas estruturas de repetição realizadas acima vão dar o mesmo resultado.

"""
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi demais')
"""

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi demais')

#Dessa forma vai mostrar a posição de cada elemento.

print(sorted(lanche))

#Utilizando sorted() vai organizar as tuplas em ordem, se for elemento númerico em ordem crescente, se for alfabético em ordem alfabética.

print(sorted(lanche, reverse=True))

#O reverse=True vai colocar na ordem contrária do sorted()
