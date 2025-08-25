#Estruturas de repetição(while).

#63 - Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros elementos de uma sequência de Fibonacci.

n = int(input('Digite quantos numeros vão para a sequencia: '))
antigo = 0
novo = 1
seq = 0
c = 1
while c <= n:                                       #Nesta linha o loop vai continuar até a variável c chegar no mesmo valor da variável n
    print(seq, end=' ')                             #Imprime o primeiro valor da sequência
    seq = novo + antigo                             #Soma a variável seq com a variável novo e a variável antigo para mostrar o proximo valor
    antigo = novo                                   #A variável antigo passa a ser a variável novo
    novo = seq                                      #A variável novo passa a ser a variável seq para dar continuidade
    c += 1
#O erro deste exercício é que não aparece o segundo valor da sequência(0, 1, 1)


#Correção

"""
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end=' ')
cont = 3
while cont <= n:                                    #Nesta linha o loop vai continuar até a variável cont chegar no mesmo valor da variável n
    t3 = t1 + t2                                    #Soma dos valores para a sequência
    print(f' -> {t3}', end=' ')
    t1 = t2                                         #A variável t1 passa a ser a variável t2
    t2 = t3                                         #A variável t2 passa a ser a variável t3
    cont += 1
print(' -> FIM')

#Resolvido o problema de não mostrar o valor entre 0 e 1 da sequência
"""
