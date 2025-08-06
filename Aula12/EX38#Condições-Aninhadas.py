#Condições Aninhadas.

num1 = int(input('Escolha o valor: '))
num2 = int(input('Escolha o valor: '))
if num1 > num2:
    print('O valor {} é maior que o valor {}'.format(num1, num2))
elif num2 > num1:
    print('O valor {} é maior que o valor {}'.format(num2, num1))
else:
    print('Os valores são iguais')