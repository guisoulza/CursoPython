#Tuplas

#72 - Crie um programa que tenha uma tupla totalmente preenchida por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por exteso.

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
usuario = int(input('Digite um número de 0 a 20: '))
print(f'O numero digitado por extenso é {numeros[usuario]}')