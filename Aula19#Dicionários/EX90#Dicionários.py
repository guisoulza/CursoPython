# Dicionários

# 90 - Faça um programa que leia nome e média de um aluno, guardando tambem a situação em um dicionário. No final mostre
# o conteúdo da estrutura na tela.

boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['média'] = int(input(f'Média do {boletim["nome"]}: '))
print('-=' * 30)
print(f' - O nome é igual a {boletim['nome']}')
print(f' - Média é igual a {boletim['média']}')
if boletim['média'] < 7:
    print(' - Situação é Recuperação')
else:
    print(' - situação é Aprovado')

# Correção

"""
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
"""