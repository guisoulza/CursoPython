#Condições Aninhadas.

#39 - Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:

#Se ele ainda vai se alistar ao serviço militar;
#Se é a hora de se alistar;
#Se já passou do tempo de alistamento.

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