#Primeiros Comandos em python.

#02 - Crie um script que leia o dia, o mês e o ano de uma pessoa e mostre uma mensagem com data formatada.

dia = int(input('Dia de nascimento: '))
mes = int(input('Mes de nascimento: '))
ano = int(input('Ano de nascimento: '))
print('Você nasceu em {}/{}/{}'.format(dia,mes,ano))