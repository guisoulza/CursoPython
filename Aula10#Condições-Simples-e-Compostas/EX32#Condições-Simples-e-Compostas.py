#Condições Simples e Compostas.

from datetime import date

a = int(input('Digite o ano: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('\033[4;32mO ano {} é bissexto\033[m'.format(a))
else:
    print('\033[4;31mO ano {} não é bissexto\033[m'.format(a))






'''
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
'''