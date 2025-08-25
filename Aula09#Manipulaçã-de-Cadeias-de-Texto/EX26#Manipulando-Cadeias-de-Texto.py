#Manipulando Cadeias de Texto.

#26 - Faça um programa que leia uma frase pelo teclado e mostre:

#Quantas vezes aparece a letra "A";
#Em que posição ela aparece a primeira vez;
#Em que posição ela aparece a última vez;

frase=str(input('Digite a frase: ')).strip().upper()
print(frase.count('A'))
print(frase.find('A')+1)                                                #O +1 é só para mostrar a posição começando em 1, já que Python começa a contar do 0.
print(frase.rfind('A')+1)                                               #rfind() procura o último índice em que a letra 'A' aparece.
