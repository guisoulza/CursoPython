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