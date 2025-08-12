#Estruturas de repetição(for).

somaidade = 0
mediaidade = 0
maisvelho = 0
nomevelho = ''
totmulher = 0
for i in range(1, 5):
    print(f'-----{i}º Pessoa-----')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
print('--------------------')
mediaidade = somaidade / 4
print(f'A média de idade é {mediaidade} anos')
print(f'O homem mais velhor tem {maisvelho} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos')

