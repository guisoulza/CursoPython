#Manipulando Cadeias de Texto.

#24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade=str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')                    #Vai mostrar o valor booleano se a palavra começar com "SANTO", colocado upper() para não dar erro se o usuário digitar em minúsculo ou maiúsculo.
#print('Tem Santo? {}'.format('Santo' in cidade))