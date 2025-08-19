#Interrompendo Repetições while.

#71 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual valor será sacado (número inteiro) e o programa deve informar quantas cédulas de cada valor serão entregues. OBS: Caixa possui notas de 50, 20, 10 e 1.

n = int(input('Digite o valor do saque: '))
if n // 50 > 0:
    print(f'Total de {n // 50} cédulas de 50.')