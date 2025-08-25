#Estruturas de repetição(for).

#55 - Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos.

maior = 0                                                       #Inicializa as variáveis para armazenar maior e menor peso.
menor = 0
for i in range(1, 6):
    p = float(input(f'Digite o peso da {i}º pessoa: '))
    if i == 1:                                                  #No primeiro ciclo, o peso digitado é tanto o maior quanto o menor.
        maior = p
        menor = p
    else:
        if p > maior:                                           #Se o peso atual for maior que o maior registrado.
            maior = p                                           #Atualiza o maior peso.
        if p < menor:                                           #Se o peso atual for menor que o menor registrado.
            menor = p                                           #Atualiza o menor peso.
print(f'O maior peso é {maior}Kg')
print(f'O menor peso é {menor}Kg')






