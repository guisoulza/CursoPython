#Condições Simples e Compostas.

from random import randint
from time import sleep

c = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
j=int(input('Qual número pensei?\n'))
print('\033[4;35mPROCESSANDO...\033[m')
sleep(2)
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