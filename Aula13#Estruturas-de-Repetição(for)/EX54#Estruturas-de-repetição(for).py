#Estruturas de repetição(for).

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(0, 8):
    a = int(input(f'Qual ano a {i}º nasceu?\n'))
    n = atual - a
    if n < 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Temos {totmaior} pessoas maiores de idade')
print(f'Temos {totmenor} pessoas menores de idade')