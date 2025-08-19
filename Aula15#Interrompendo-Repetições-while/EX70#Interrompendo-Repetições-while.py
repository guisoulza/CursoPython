#Interrompendo Repetições while.

#70 - Crie um programa que leia o nome e o preço de vários produtos. O Programa deverá perguntar se o usuário vai continuar. No final mostre:
#* Total gasto na compra;
#* Quantos produtos custam mais de R$1000;
#* Qual produto mais barato.

c = soma = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    soma += valor
    if valor >= 1000:
        c += 1
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao not in 'SN':
        print('Opção inválida')
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'O total das compras é R${soma:.2f}, com {c} produtos maiores que R$1000,00 e o produto mais barato é.')
