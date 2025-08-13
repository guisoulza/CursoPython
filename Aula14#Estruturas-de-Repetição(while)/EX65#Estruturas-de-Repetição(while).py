#Estruturas de repetição(while).

n = int(input('Digite um valor: '))
soma = n
c = 1
maior = n
menor = n
d = 'S'
while d != 'N':                                                 #Loop vai continuar até o usuário digitar N
    d = input('Deseja continuar? [S/N] ').upper().strip()
    if d != 'S' and d != 'N':                                   #Condição para se o usuário digitar algo que não foi solicitado
        print('Opção invalida!')
    if d == 'S':                                                #Condição para repetir o loop quando o usuário digitar S
        n = int(input('Digite um valor: '))
    soma = soma + n
    c += 1
    if n > maior:                                               #Condição para mostrar o maior valor
        maior = n
    if n < menor:                                               #Condição para mostrar o menor valor
        menor = n
media = soma / c
print(f'''A média desses valores é {media}. 
O maior é {maior} e o menor é {menor}.''')

#Correção

"""
resp = 'S'
soma = quant = media = 0
while resp in 'Ss':                                             #Loop vai continuar enquanto o usuário digitar S
    num = int(input('Digite um número: '))       
    soma += num
    quant += 1
    if quant == 1:                                              #Condição para igualar as variaveis
        maior = menor = num
    else:
        if num > maior:                                         #Condição para mostrar o maior valor
            maior = num
        if num < menor:                                         #Condição para mostrar o menor valor
            menor = num
    resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
media = soma / quant
print(f'''Você digitou {quant} números e a média é {media}
O maior é {maior} e o menor é {menor}.''')

#Aparentemente a forma que eu fiz ficou mais completa por mais que a forma do professor seja mais simples.
"""
