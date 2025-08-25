#Condições Aninhadas.

#36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comproador e em quantos anos ele pretende pagar. Calcule o valor da prestação sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da Casa: '))
salario = float(input('Qual o salário?\n'))
ano = int(input('Quantos anos?\n'))
exceder = salario / 100 * 30
prestacao = casa / (ano * 12)
print('Em {} será no valor de R${:.2f} por mes'.format(ano, prestacao))
if exceder < prestacao:
    print('Emprestimo Negado')
else:
    print('Emprestimo Aprovado')