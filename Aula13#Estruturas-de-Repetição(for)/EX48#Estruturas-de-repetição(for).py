#Estruturas de repetição(for).

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont = cont + 1
'''for c in range(0, 501):
    if c % 3 == 0:
        if c % 2 == 1:
            s += c'''
print(f'A soma de todos os {cont} números é {s}')
