#Interrompendo Repetições while.

#71 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual valor será sacado (número inteiro) e o programa deve informar quantas cédulas de cada valor serão entregues. OBS: Caixa possui notas de 50, 20, 10 e 1.

print('-' * 30)
print(f'{'GELAS BANK':^30}')
print('-' * 30)
n = int(input('Digite o valor do saque: '))
cedula = 50
total_cedula = 0
nota50 = nota20 = nota10 = nota1 = 0
while True:
    if n >= cedula:
        n -= cedula
        total_cedula += 1
    else:
        if cedula == 50:
            nota50 = total_cedula
            cedula = 20
            print(f'Serão necessárias {total_cedula} notas de 50.')
        elif cedula == 20:
            nota20 = total_cedula
            cedula = 10
            print(f'Serão necessárias {total_cedula} notas de 20.')
        elif cedula == 10:
            nota10 = total_cedula
            cedula = 1
        elif cedula == 1:
            nota1 = total_cedula
            print(f'Serão necessárias {total_cedula} notas de 1.')
        total_cedula = 0
        if n == 0:
            break

#Correção

"""
print('-' * 30)
print(f'{'BANCO CEV':^30}')
print('-' * 30)
valor = int(input('Digite o valor do saque: '))
total = valor
ced = 50
totalced = 0
while True:
    if valor >= ced:
        total -= ced
        tot ced += 1
    else:
    print(f'O total de {totced} cedulas de {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
"""