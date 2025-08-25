#Manipulando Cadeias de Texto.

#27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.

nome = str(input('Digite seu nome: ')).strip()
nome1=nome.split()
print('\033[4;34mO nome {} tem primeiro nome {} e ultimo nome {}\033[m'.format(nome, nome1[0], nome1[-1]))          #0 para começar do primeiro índice e -1 para começar do último índice.