#Estruturas de repetição(for).

#51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA(Progreção Aritmética). No final, mostre os 10 primeiros termos dessa progração.

n = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
d = n + (10 - 1) * r                                #Calcula o décimo termo da PA.
print('Progressão Aritmética: ', end='')            #Com end='', você substitui a quebra de linha por outro caractere ou nada.
for i in range(n, d + r, r):
    print(i, end=' ')                               #Imprime cada termo na mesma linha separado por espaço.