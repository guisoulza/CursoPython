# Listas

# 85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.

valor = [[], []]

for c in range(0, 7):
    numero = int(input(f'Digite o {c+1}º valor: '))
    if numero % 2 == 0:
        valor[0].append(numero)
    else:
        valor[1].append(numero)
valor[0].sort()
valor[1].sort()
print(f'Ordem dos pares: {valor[0]}')
print(f'Ordem dos impares: {valor[1]}')