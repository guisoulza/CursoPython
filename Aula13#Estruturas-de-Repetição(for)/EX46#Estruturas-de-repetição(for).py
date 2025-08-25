#Estruturas de repetição(for).

#46 - Faça um programa que mostra na tela uma contagem regrassiva para o estouro dos fogos, indo de 10 até 0 com uma pausa de um segundo.

from time import sleep
print('Se prepare para os Fogos!!!')
for c in range(10, 0-1, -1):
    sleep(1)
    print(c)
print('Feliz ano novo!!!')