#Estruturas de repetição(for).

#50 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas dos pares. Se o valor for impar desconsidere-o.

s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:                              #Condição para selecionar apenas os números pares.
        s += n
        cont += 1
    else:
        print('Não adicionado')
print(f'Foi informado {cont} números pares e a soma foi {s}')

