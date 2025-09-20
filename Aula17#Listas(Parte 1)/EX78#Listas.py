# Listas.

# 78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

lista = []
for c in range(0, 5):
    usuario = int(input('Digite um valor: '))
    lista.append(usuario)
print(f'O maior valor é {max(lista)}')
print(f'E está na posição {lista.index(max(lista)) + 1}º')
print(f'O menor valor é {min(lista)}')
print(f'E está na posição {lista.index(min(lista)) + 1}º')

# Correção

"""
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
"""