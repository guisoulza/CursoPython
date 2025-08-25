#Estruturas de repetição(for).

#47 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Contagem de números pares')
for c in range(2, 50+1, 2):
    print(c, end=' ')

'''for c in range(1, 50+1):
    if c % 2 == 0:
        print(c, end=' ')'''