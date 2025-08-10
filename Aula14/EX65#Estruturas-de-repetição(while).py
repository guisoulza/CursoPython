#Estruturas de repetição(while).

n = int(input('Digite um valor: '))
soma = n
c = 1
maior = n
menor = n
d = 'S'
while d != 'N':
    d = input('Deseja continuar? [S/N] ').upper().strip()
    if d == 'S':
        n = int(input('Digite um valor: '))
    soma = soma + n
    c += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n

media = soma / c
print(f'A média desses valores é {media} e o maior é {maior} e o menor é {menor}')