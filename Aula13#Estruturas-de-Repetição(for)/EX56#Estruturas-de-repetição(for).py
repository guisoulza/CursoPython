#Estruturas de repetição(for).

#56 - Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#A média de idade;
#Qual o nome do homem mais velho;
#Quantas mulheres tem menos de 20 anos.

somaidade = 0                                                       #Soma das idades para calcular a média.
mediaidade = 0                                                      #Média de idade (será calculada depois).
maisvelho = 0                                                       #Armazena a idade do homem mais velho.
nomevelho = ''                                                      #Armazena o nome do homem mais velho.
totmulher = 0                                                       #Contador de mulheres com menos de 20 anos
for i in range(1, 5):
    print(f'-----{i}º Pessoa-----')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':                                     #Verifica se é o primeiro homem e inicializa o mais velho.
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maisvelho:                          #Atualiza o homem mais velho se a idade for maior.
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:                                 #Conta mulheres com menos de 20 anos
        totmulher += 1
print('--------------------')
mediaidade = somaidade / 4
print(f'A média de idade é {mediaidade} anos')
print(f'O homem mais velhor tem {maisvelho} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos')

