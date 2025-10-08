# Operadores Aritiméticos (Arithmetic Operators).

# 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# 12 - Make a algorithm that reads the price of a product and show the new price, with 5% of discount.

p=float(input('Valor do produto: R$'))
#c=float((p/100)*5)
#d=float(p-c)
d=p-(p*5/100)
print('Com o desconto de 5% fica por R${:.2f}'.format(d))

