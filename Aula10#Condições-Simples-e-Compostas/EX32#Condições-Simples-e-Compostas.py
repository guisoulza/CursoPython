#Condições Simples e Compostas.

#32 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date                                           #datetime é um módulo padrão do Python que permite trabalhar com datas, horários e timestamps de forma mais avançada que o módulo time.

a = int(input('Digite o ano: '))
if a == 0:
    a = date.today().year                                           #Retorna um objeto date representando a data de hoje (year = ano, month = mês e day = dia).
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('\033[4;32mO ano {} é bissexto\033[m'.format(a))
else:
    print('\033[4;31mO ano {} não é bissexto\033[m'.format(a))

#Correção

"""
from datetime import date

a = int(input('Digite o ano: '))
if a == 0:
    a = date.today().year
if a % 400 == 0:
    print('O ano é bissexto')
else:
    if a % 100 == 0:
        print('O ano não é bissexto')
    else:
        if a % 4 == 0:
            print('O ano é bissexto')
        else:
            print('O ano não é bissexto')
"""