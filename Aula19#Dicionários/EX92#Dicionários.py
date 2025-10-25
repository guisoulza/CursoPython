# Dicionários

# 92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário se por acaso a CTPS for diferente de 0, o dicionário receberá tambem o ano de contratação e o salário.
# Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['Nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - dados['Nascimento']
dados['CTPS'] = int(input('CTPS (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = int(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Contratação'] - dados['Nascimento']) + 35

print('-=' * 30)
for k, v in dados.items():
    if k != 'Nascimento':
        print(f' - {k} tem o valor {v}')
