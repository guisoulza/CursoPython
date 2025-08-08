from random import randint
from time import sleep

c = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
j = None
while j != c:
    j=int(input('Qual número pensei?\n'))
    print('\033[4;35mPROCESSANDO...\033[m')
    sleep(2)
    if j == c:
        print('\033[4;32mParabéns, você acertou!!\033[m')
    else:
        print('\033[4;31mVocê errou, tente novamente!!\033[m'.format(c))
print('Fim')