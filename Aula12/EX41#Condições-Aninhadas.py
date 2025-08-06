#Condições Aninhadas.

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