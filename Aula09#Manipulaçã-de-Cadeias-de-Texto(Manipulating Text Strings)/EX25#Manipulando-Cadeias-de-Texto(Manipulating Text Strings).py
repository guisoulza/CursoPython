# Manipulando Cadeias de Texto (Manipulating Text Strings).

# 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

# 25 - Create a program that reads a person's name and says whether they have "Silva" in their name.

nome=str(input('Digite o nome: ')).strip()
print('Tem Silva? {}'.format('silva' in nome.lower()))          #Vai mostrar o valor booleano se a palavra começar com "silva", colocado lower() para não dar erro se o usuário digitar em maiúsculo ou maiúsculo.
