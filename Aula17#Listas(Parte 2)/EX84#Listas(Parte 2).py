# Listas

#84 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# * Quantas pessoas foram cadastradas.
# * Uma listagem com as pessoas mais pesadas(+100kg).
# * Uma listagem com as pessoas mais leves(-70kg).

pessoas = []
dados = []
pesados = []
leves = []
totpessoas = 0

while True:
    nome = str(input('Nome: '))
    totpessoas += 1
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Foram cadastradas {totpessoas} pessoas')
for p in pessoas:
    if p[1] > 100:
        pesados.append(p[0])
    if p[1] < 70:
        leves.append(p[0])

print(f'{pesados} estão com mais de 100 kg.')
print(f'{leves} estão com menos de 70 kg.')

# Correção

"""
temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])
    if len(temp) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo. você cadastrou {len(pessoas)} pessoas. ')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
"""