# Dicionários

# 95 - Aprimore o exercício 93 para que ele funcione com vários jogadores incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

jogador = []
while True:
    futebol = {}
    gols = []
    futebol['Nome'] = str(input('Nome do jogador: '))
    futebol['partidas'] = int(input('Quantas partidas jogadas: '))
    for partida in range(futebol['partidas']):
        gols.append(int(input(f'     Quantos gols na partida {partida + 1}: ')))
        futebol['gols'] = gols
        futebol['total'] = sum(gols)
    jogador.append(futebol.copy())
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'{"COD":<4}{"NOME":<15}{"GOLS":<20}{"TOTAL":<5}')
print('-' * 50)
for j in range(len(jogador)):
    print(f'{j:<4}{jogador[j]["Nome"]:<15}{str(jogador[j]["gols"]):<20}{jogador[j]["total"]:<5}')
print('-' * 50)
while True:
    data = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if data == 999:
        print('FINALIZANDO...')
        break
    if data >= len(jogador):
        print(f'ERRO! Não existe jogador com o código {data}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador[data]["Nome"]}:')
        for i in range(len(jogador[data]['gols'])):
            print(f' =>  Na partida {i + 1}, fez {jogador[data]["gols"][i]} gols.')
