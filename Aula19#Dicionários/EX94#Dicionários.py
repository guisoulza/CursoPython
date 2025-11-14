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
    dados['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
    if dados['Sexo'] not in 'FfMm':
        print('Genero invalido tente novamente.')
        dados['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
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

# Correção

"""
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa.append(str(input('Nome: ')))
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
        if pessoa['sexo'] in 'FfMm':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas M ou F.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'[{p["Nome"]}] ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
"""