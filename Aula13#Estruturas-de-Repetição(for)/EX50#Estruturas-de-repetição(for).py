#Estruturas de repetição(for).

s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
    else:
        print('Não adicionado')
print(f'Foi informado {cont} números pares e a soma foi {s}')

