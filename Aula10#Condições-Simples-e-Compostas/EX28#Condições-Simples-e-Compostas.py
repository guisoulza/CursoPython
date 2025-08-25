#Condições Simples e Compostas.

#28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual o número escolhido pelo computador. O programa deve dizer se venceu ou perdeu.

from random import randint
from time import sleep                                                #time é um módulo padrão do Python que permite trabalhar com tempo, datas e pausas.

c = randint(0,5)                                                #O randint(a, b) gera um número inteiro aleatório entre a e b, incluindo ambos os limites.
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
j=int(input('Qual número pensei?\n'))
print('\033[4;35mPROCESSANDO...\033[m')
sleep(2)                                                              #sleep() é uma função do módulo time que faz o programa “dormir” por um certo tempo.
if j == c:
    print('\033[4;32mParabéns, você acertou!!\033[m')
else:
    print('\033[4;31mVocê errou, eu pensei em {}, tente novamente!!\033[m'.format(c))





'''from random import choice

n=[1, 2, 3, 4, 5]
m=choice(n)
c=int(input('Qual o numero? '))
if c == m:
    print('Você acertou!')
else:
    print('Você errou!')
print('O numero é {}'.format(m))'''