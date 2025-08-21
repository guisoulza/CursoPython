#Interrompendo Repetições while.

#68 - Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('Vamos jogar par ou impar?')
print('-' * 18)
comp = randint(0, 100)
soma = cont = 0
while True:
    n = int(input('Digite o número: '))
    j = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    if j not in 'PI':
        print('Opção inválida. Tente novamente.')
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
            break
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

#Correção

"""
from random import randint

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes!')
"""
