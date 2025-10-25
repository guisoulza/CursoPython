# Dicionários

# 93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário incluindo o total de gols feitos durante o campeonato.

futebol = {}
gols = []
c = 0
futebol['Nome'] = str(input('Nome do jogador: '))
futebol['partidas'] = int(input('Quantas partidas jogadas: '))
for partida in range(futebol['partidas']):
    gols.append(int(input(f'     Quantos gols na partida {c+1}: ')))
    c += 1
    futebol['gols'] = gols
    futebol['total'] = sum(gols)
print('-=' * 30)
print(futebol)
print('-=' * 30)
for k, v in futebol.items():
    if k != 'partidas':
        print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {futebol['Nome']} teve {futebol["partidas"]} partidas')
for partida in range(futebol['partidas']):
    print(f'     =>Na partida {partida + 1} fez {futebol["gols"][partida]} gols.')
print(f'No total foram {futebol["total"]} gols.')
