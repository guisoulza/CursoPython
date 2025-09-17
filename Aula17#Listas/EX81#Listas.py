# Listas.

# 81 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

# * Quantos números foram digitados
# * A lista de valores, ordenada de forma decrescente.
# * Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    usuario = int(input('Digite um valor: '))
    lista.append(usuario)
    fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if fim not in 'SN':
        print('Opção inválida')
        fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    elif fim == 'N':
        break
print(f'Foram digitados {len(lista)} elementos.')
print(f'O inverso é: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')

# Correção

"""
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp not in 'SN':
        print('Opção invalida!')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    elif resp == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
"""
