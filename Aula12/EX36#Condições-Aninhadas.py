#Condições Aninhadas.

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