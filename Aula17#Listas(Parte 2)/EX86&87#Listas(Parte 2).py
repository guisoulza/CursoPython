# Listas

# 86 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a
# matriz na tela, com a formatação correta.

matriz = [[], [], []]
soma = tersoma = 0
for c in range(0, 3):
    for i in range(0, 3):
        valor = int(input(f'Digite um valor: '))
        if valor % 2 == 0:
            soma += valor
        matriz[c].append(valor)
print('-=' * 25)
print('Matriz:')
for linha in matriz:
    for elemento in linha:
        print(f'[ {elemento:^5} ]', end='')
    print()

# 87 - Aprimore o desafio anterior, mostrando no final:
# * A soma de todos os valores pares digitados.
# * A soma dos valores da terceira coluna.
# * O maior valor da segunda linha.

print('-=' * 25)
print(f'A soma dos valores pares é: {soma}')
tersoma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é: {tersoma}')
print(f'O maior número da segunda linha é: {max(matriz[1])}')

# Correção

"""
matriz = [[0, 0 ,0], [0, 0 ,0], [0, 0 ,0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é: {mai}')
"""

