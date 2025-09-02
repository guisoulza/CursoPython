#Tuplas

#76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (
    ("Arroz", 10.50),
    ("Feijão", 8.90),
    ("Macarrão", 6.20),
    ("Carne", 35.00),
    ("Leite", 4.80),
    ("Pão", 7.50),
    ("Queijo", 15.00),
    ("Café", 12.90)
)
print(f'\n{'Tabela de preços': ^39}')
print('-' * 39)
for n in produtos:
    print(f'{n[0]:.<30}R$:{n[1]:.2f}')