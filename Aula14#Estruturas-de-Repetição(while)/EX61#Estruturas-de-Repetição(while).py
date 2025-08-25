#Estruturas de repetição(while).

#61 - Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progreção utilizando a estrutura while.

n = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
termo = n
cont = 1
print('Progressão Aritmética: ', end='')
while cont <= 10:                                     #Nesta linha o loop vai parar quando a variável contadora chegar a 10
    print(termo, end=' ')
    termo += r                                        #A variável termo é incrementada com a variável r
    cont += 1                                         #Adiciona +1 a variável contadora para controle do loop

#Correção

"""
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:                                     #Nesta linha o loop vai parar quando a variável contadora chegar a 10
    print(f'{termo} -> ', end='')
    termo += razao                                    #A variável termo é incrementada com a variável r
    cont += 1                                         #Adiciona +1 a variável contadora para controle do loop
print('FIM')

"""
