#Manipulando Cadeias de Texto.

#25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome=str(input('Digite o nome: ')).strip()
print('Tem Silva? {}'.format('silva' in nome.lower()))          #Vai mostrar o valor booleano se a palavra começar com "silva", colocado lower() para não dar erro se o usuário digitar em maiúsculo ou maiúsculo.
