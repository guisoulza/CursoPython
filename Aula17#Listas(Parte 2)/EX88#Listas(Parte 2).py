# Listas (Parte 2)

# 88 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

quant = int(input('Quantos jogos você deseja?\n'))
sorteio = list()
print('-=' * 30)
for c in range(0, quant):
    numeros = list()
    while len(numeros) < 6:
        n = (randint(1, 60))
        if n not in numeros:
            numeros.append(n)
    sorteio.append(numeros[:])
    sleep(0.75)
    print(f'{c + 1}º jogo: {sorteio[c]}')
print('-=' * 30)

