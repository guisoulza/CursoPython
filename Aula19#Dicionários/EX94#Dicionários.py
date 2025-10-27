# Dicionários

# 94 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final mostre:
#
# * Quantas pessoas foram cadastradas.
# * A média de idade do grupo.
# * Uma lista com todas as mulheres.
# * Uma lista com todas as pessoas com idade acima da média.

dado = []
mulheres = []
idademed = []
c= medidade = total = 0
while True:
    dados = {}
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo: '))
    if dados['Sexo'] not in 'FfMm':
        print('Genero invalido tente novamente.')
        dados['Sexo'] = str(input('Sexo: '))
    dados['Idade'] = int(input('Idade: '))
    dado.append(dados.copy())
    c += 1
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {c} pessoas.')
for p in dado:
    total += p['Idade']
    medidade = total / c
print(f'A média de idade é {medidade:.2f} anos.')
for p in dado:
    if p['Sexo'] == 'F':
        mulheres.append(p['Nome'])
print(f'Lista de mulheres cadastradas: {", ".join(mulheres)}')
for p in dado:
    if p['Idade'] >= medidade:
        idademed.append(p['Nome'])
print(f'Pessoas acima da média: {", ".join(idademed)}')
print('-=' * 30)





