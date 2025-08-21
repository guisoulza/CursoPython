#Interrompendo Repetições while.

#70 - Crie um programa que leia o nome e o preço de vários produtos. O Programa deverá perguntar se o usuário vai continuar. No final mostre:
#* Total gasto na compra;
#* Quantos produtos custam mais de R$1000;
#* Qual produto mais barato.

cmil = soma = menor = c = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: R$'))
    c += 1
    soma += valor
    if valor >= 1000:
        cmil += 1
    if c == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao not in 'SN':
        print('Opção inválida')
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'O total das compras é R${soma:.2f}, com {cmil} produtos maiores que R$1000,00 e o produto mais barato é {barato}.')

#Correção

"""
total = totmil = menor = c = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$'))
    cont += 1
    total += preco
    if preco >= 1000:
        totmil += preco
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA)
print(f'O total da compra foi R${total:.2f}')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f})
"""