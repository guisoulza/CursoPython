#Estruturas de repetição(while).

#64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor "999", que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

c = 0
soma = 0
n = int(input('Digite um valor (999 para parar): '))
while n != 999:                                                                 #Loop para continuar mostrando valores até o usuário digitar 999
        soma += n                                                               #Realiza primeiro a incrementação entre as variáveis soma e n
        n = int(input('Digite um valor (999 para parar): '))                    #Como a variável de leitura n foi adicionada depois o loop seguirá a ordem das linhas
        c += 1
print(f'Foram digitados {c} números e a soma dos valores é {soma}')

#Correção

"""
num = cont = soma = 0
num = int(input('Digite um valor (999 para parar): '))
while num != 999:                                                               #Loop para continuar mostrando valores até o usuário digitar
    soma += num                                                                 #Realiza primeiro a incrementação entre as variáveis soma e n
    cont += 1
    num = int(input('Digite um valor (999 para parar): '))                      #Como a variável de leitura n foi adicionada depois o loop seguirá a ordem das linhas
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
"""
