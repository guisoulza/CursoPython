# Listas.

# 78 - Faça um programa que leia 5 valores numéricos e guarde-os em um lista.
# No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

lista = []
for c in range(0, 5):
    usuario = int(input('Digite um valor: '))
    lista.append(usuario)
print(f'O maior valor é {max(lista)}')
print(f'E está na posição {lista.index(max(lista)) + 1}º')
print(f'O menor valor é {min(lista)}')
print(f'E está na posição {lista.index(min(lista)) + 1}º')