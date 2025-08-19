#Interrompendo Repetições while.

#68 - Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

print('Vamos jogar par ou impar?')
print('-' * 18)
comp = random.randint(0, 100)
soma = cont = 0
while True:
    n = int(input('Digite o número: '))
    j = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    if j == 'P':
        print('Impar')
        soma = comp + n
        print(f'A soma é {soma}')
        if soma % 2 == 0:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu! Mais sorte na proxima')
    if j == 'I':
        print('Par')
        soma = comp + n
        print(f'A soma é {soma}')
        if soma % 2 == 1:
            print('Você ganhou!')
            cont +=1
            print('-' * 18)
        else:
            print('Você perdeu! Mais sorte na proxima.')
            break
print(f'Foram {cont} vitórias consecutivas.')
print('-' * 18)
