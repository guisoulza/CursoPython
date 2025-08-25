#Condições Aninhadas.

#41 - A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#Até 9 anos: Mirim;
#Até 14 anos: Infantil;
#Até 19 anos: Junior;
#Até 20 anos: Sênior;
#Acima: Master.

from datetime import date

nasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria é MASTER')