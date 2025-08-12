#Operadores Aritméticos.

p=float(input('Valor do produto: R$'))
#c=float((p/100)*5)
#d=float(p-c)
d=p-(p*5/100)
print('Com o desconto de 5% fica por R${:.2f}'.format(d))

