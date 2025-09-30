# Primeiros Comandos em python (First commands in Python).

# 02 - Crie um script que leia o dia, o mês e o ano de uma pessoa e mostre uma mensagem com data formatada.
# 02 - Create a script that reads a person's day, month, and year and displays a message with the formatted date.

dia = int(input('Dia de nascimento: '))
mes = int(input('Mes de nascimento: '))
ano = int(input('Ano de nascimento: '))
print('Você nasceu em {}/{}/{}'.format(dia,mes,ano))