#Tuplas

#75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

# Quantas vezes apareceu o número 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram o números pares.

tupla = ()
for i in range(0, 4):
    valor = int(input('Digite um valor: '))
    tupla += (valor,)
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 aparece na {tupla.index(3) + 1}ª posição.')
else:
    print('Não possui o número 3 na tupla.')
pares = ()
for n in tupla:
    if n % 2 == 0:
        pares += (n,)
print(f'Os pares foram: {pares}')

#Correção

"""
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o últmo número: ')))
print(f'voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não aparece na tupla')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' '))
"""



