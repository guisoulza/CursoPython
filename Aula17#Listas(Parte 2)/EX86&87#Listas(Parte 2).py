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


