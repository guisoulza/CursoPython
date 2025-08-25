#Condições Aninhadas.

#44 - Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento:

#A vista: 10% de desconto;
#Cartão a vista: 5% de desconto;
#parcelado em 2x: preço normal;
#parcelado em 3x ou mais: 20% de juros.

preco = float(input('Qual o valor do produto?\n'))
print('1 - À vista no dinheiro\n2 - À vista no cartão\n3 - 2x sem juros\n4 - 3x ou mais com 20% de juros')
formapagar = int(input('Qual a forma de pagamento?\n'))
if formapagar == 1:
    desconto = preco - (preco / 100) * 10
    print('O valor do produto é de R$ {:.2f}'.format(desconto))
elif formapagar == 2:
    desconto = preco - (preco / 100) * 5
    print('O valor do produto é R$ {:.2f}'.format(desconto))
elif formapagar == 3:
    print('O valor do produto é R$ {:.2f}'.format(preco))
elif formapagar == 4:
    juros = preco / 100 * 30 + preco
    print('O valor do produto é R$ {:.2f}'.format(juros))
else:
    print('Erro!')