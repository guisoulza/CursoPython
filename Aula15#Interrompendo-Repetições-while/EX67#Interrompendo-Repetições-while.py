#Interrompendo Repetições while.

#67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. o programa será interrompido quando o número solicitado for negativo.

print('Tabuada')
c = 1
n = -1
while True:
    tabuada = int(input('Digite o número para a tabuada (digite um número negativo para parar):'))
    print('-' * 12)
    if tabuada <= -1:
        break
    while True:
        m = tabuada * c
        print(f'{tabuada} x {c} = {m}')
        c += 1
        if c == 11:
            break
    print('-' * 12)
print('Fim')

#Correção

"""
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n <= -1:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('Tabuada encerrada! Volte sempre!')
"""