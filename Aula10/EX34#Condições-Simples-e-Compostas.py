#Condições Simples e Compostas.

s = float(input('Digite o salário: '))
if s <= 1250:
    print('O valor do aumento é R${:.2f}'.format(s / 100 * 10))
    print('O novo salário é de R${:.2f}'.format(s / 100 * 10 + s))
else:
    print('O valor do aumento é R${:.2f}'.format(s / 100 * 15))
    print('O novo salário é de R${:.2f}'.format(s / 100 * 15 + s))