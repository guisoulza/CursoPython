#Condições Aninhadas.

#45 - Faça um JOKENPO.

from random import choice

print('JOKENPO')
escolha = str(input('Qual a sua escolha?\n'))
jokenpo = ['Pedra' , 'Papel' , 'Tesoura']
result = choice(jokenpo)
if result == 'Pedra' and escolha == 'Papel':
    print(result)
    print('Você Ganhou!')
elif result == 'Tesoura' and escolha == 'Pedra':
    print(result)
    print('Você Ganhou!')
elif result == 'Papel' and escolha == 'Tesoura':
    print(result)
    print('Você Ganhou!')
else:
    print(result)
    print('Você Perdeu!')