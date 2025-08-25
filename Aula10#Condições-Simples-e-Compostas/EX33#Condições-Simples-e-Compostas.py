#Condições Simples e Compostas.

#33 - Faça um programa que leia 3 números e mostre qual é maior e qual é menor.

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))

menor = a
if b<a and b<c:                                             #Verifica se 'b' é menor que 'a' e 'c'.
    menor = b                                               #Atualiza 'menor' para 'b' se for realmente menor.
if c<a and c<b:                                             #Verifica se 'c' é menor que 'a' e 'b'.
    menor = c                                               #Atualiza 'menor' para 'c' se for realmente menor.
maior = a
if b>a and b>c:                                             #Verifica se 'b' é maior que 'a' e 'c'.
    maior = b                                               #Atualiza 'maior' para 'b' se for realmente maior.
if c>a and c>b:                                             #Verifica se 'c' é maior que 'a' e 'b'.
    maior = c                                               #Atualiza 'maior' para 'c' se for realmente maior.
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))