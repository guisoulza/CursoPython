#Interrompendo Repetições while.

#66 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor "999", que é a condição de parada. No final, mostre quantos números foram digitado e qual foi a soma entre eles (desconsiderando o flag).

c = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'foram contabilizados {c} números e a soma entre eles é {soma}')

#Correção

"""

Forma incorreta:

num = soma = 0
while num != 999:
    num = int(input('Digite um valor (999 para parar): '))
    soma += num
soma -= 999
print(f'A soma dos valores foi {soma}')

Forma correta:

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}')
"""