#Interrompendo Repetições while.

#70 - Crie um programa que leia o nome e o preço de vários produtos. O Programa deverá perguntar se o usuário vai continuar. No final mostre:
#* Total gasto na compra;
#* Quantos produtos custam mais de R$1000;
#* Qual produto mais barato.

cmil = soma = menor = c = 0                                     #"cmil" é o contador de produtos com preço >= 1000, "soma" soma total dos valores dos produtos, "menor" armazena o menor valor registrado e "c" é o contador de produtos.
barato = ''                                                     #Nome do produto mais barato.
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: R$'))
    c += 1
    soma += valor
    if valor >= 1000:                                           #Conta produtos com preço >= 1000
        cmil += 1
    if c == 1:                                                  #Verifica o primeiro produto ou atualiza o mais barato.
        menor = valor                                           #Inicializa 'menor' com o valor do primeiro produto.
        barato = produto                                        #Inicializa 'barato' com o nome do primeiro produto.
    else:
        if valor < menor:                                       #Se o valor atual for menor que o menor registrado.
            menor = valor                                       #Atualiza o menor valor.
            barato = produto                                    #Atualiza o nome do produto mais barato.
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
        totmil += 1
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
print(f'Existem {totmil} produtos maiores que R$1000')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
"""
