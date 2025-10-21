# Dicionários

# 91 - Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

dado = {}
p = 0
for c in range(0, 4):
    dado[f'jogador {c+1}'] = randint(1, 6)
    print(f'jogador {c+1} tirou {dado[f'jogador {c+1}']} no dado.')
    sleep(1)
for i in range(len(dado)):
    maior = max(dado.values())
    for k in dado:
        if dado[k] == maior:
            p += 1
            print(f'{p}º Lugar: {k} com {maior}')
            dado[k] = -1
            break