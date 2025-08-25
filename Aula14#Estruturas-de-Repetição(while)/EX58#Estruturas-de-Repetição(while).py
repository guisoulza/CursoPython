#Estruturas de repetição(while).

#58 - Melhore o jogo do exercício 028 onde o computador vai "pensar" em um número de 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

c = randint(0,10)                #Variável que vai escolher um número aleatório entre 0 e 10
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
j = None                               #Variável que vai realizar o jogo
while j != c:
    j=int(input('Qual número pensei?\n'))
    print('\033[4;35mPROCESSANDO...\033[m')
    sleep(2)                           #Pausa por 2 segundos para não aparecer a resposta instantâneamente
    if j == c:                         #Condição para igualar a resposta do usuário com o computador
        print('\033[4;32mParabéns, você acertou!!\033[m')
    else:
        print('\033[4;31mVocê errou, tente novamente!!\033[m')
print('Fim')

#Correção

"""
from random import randint
computador = randint(0,5)              #Variável que vai escolher um número aleatório entre 0 e 10
print('Sou seu computador... Acabei de pensar em um número de 0 e 10.')
print('Será que consegue acertar?')
acertou = False                        #Variável com valor falso para iniciar o loop
palpite = 0                            #Variável contadora de palpites
while not acertou:
    jogador = int(input('Qual é o seu palpite?\n'))
    palpite += 1
    if jogador == computador:          #Condição para se o usuário acertar o número selecionado
        acertou = True
    else:
        if jogador < computador:       #Condição adicionada pelo professor para ter uma dica sobre o número selecionado
            print('Mais... Tente outra vez...')
        elif jogador > computador:
            print('Menos... Tente outra vez...')
print(f'Acertou com {palpite} tentativas. Parabéns!!!')

"""
