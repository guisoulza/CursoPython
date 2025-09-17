# Listas.

# 82 - Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if fim not in 'SN':
        print('Opção invalida! Tente novamente.')
        fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    elif fim == 'N':
        break
impar = []
par = []
for item in lista:
    if item % 2 == 0:
        par.append(item)
    else:
        impar.append(item)
print(f'Lista: {lista}')
print(f'Lista de pares: {par}')
print(f'Lista de impares: {impar}')