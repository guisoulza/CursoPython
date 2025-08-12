#Condições Aninhadas.

from datetime import date

nasc = int(input('Em que ano nasceu?\n'))
idade = date.today().year - nasc
if idade < 18:
    print('Ainda não está na sua época de alistamento')
    print('Seu alistamento será em {} ano(s)'.format(idade - 18))
elif idade == 18:
    print('Esta na hora de se alistar')
elif idade > 18:
    print('Alistamento pendente')
    print('Seu alistamento era para ser feito há {} ano(s)'.format(idade - 18))