# Listas.

# 79 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

lista = []
while True:
    usuario = int(input('Digite um valor: '))
    if usuario not in lista:
        lista.append(usuario)
        print('Valor adicionado na lista')
    else:
        print('Valor ja foi adicionado na lista')
    fim = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if fim not in 'SN':
        print('Opção invalida')
        fim = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    elif fim == 'N':
        break
print(f'Os valores digitados foram {sorted(lista)}')

# Correção

"""
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado na lista! Não será adicionado')
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r not in 'SN':
        print('Opção invalida! Tente novamente.')
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    elif r in 'N':
        break
print('-=' * 30)
numeros.sort()
print(f'Voce digitou os valores: {numeros}')
"""
