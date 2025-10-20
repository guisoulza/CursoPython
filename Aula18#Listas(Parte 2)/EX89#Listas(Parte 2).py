# Listas (Parte 2)

# 89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

boletim = []
while True:
    Aluno = str(input('Digite o nome do aluno: ')).title().strip()
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    alunos = list()
    alunos.append(Aluno)
    alunos.append(nota1)
    alunos.append(nota2)
    alunos.append((nota1 + nota2) / 2)
    boletim.append(alunos[:])
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f"{'Nº':<4} {'Nome':<12} {'Média':>5}")
for i, aluno in enumerate(boletim):
    print(f"{i:<4} {aluno[0]:<12} {aluno[3]:>5.1f}")
while True:
    selecao = int(input('Mostrar nota de qual aluno? (999 para parar): '))
    if selecao == 999:
        break
    else:
        print(f'Notas de {boletim[selecao][0]} são {boletim[selecao][1]} {boletim[selecao][2]}')
print('-=' * 30)

# Correção

"""
ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: ')).title().strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 35)
    opc = int(input('Mostrar nota de qual aluno? (999 para parar): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]} {ficha[opc][2]}')
"""