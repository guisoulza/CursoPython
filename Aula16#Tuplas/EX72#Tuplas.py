#Tuplas

#72 - Crie um programa que tenha uma tupla totalmente preenchida por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por exteso.

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
usuario = int(input('Digite um número de 0 a 20: '))
while True:
    if usuario > 20:
        print('Tente novamente!')
        usuario = int(input('Digite um número de 0 a 20: '))
    print( f'O numero digitado por extenso é {numeros[usuario]}')                  # Sempre lembrar que a tupla pode reconhecer dado do usuário se estiver nos [].
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        print('Tente novamente. ', end='')
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'S':
        usuario = int(input('Digite um número de 0 a 20: '))
    if opcao == 'N':
        break

#O professor passou um desafio bônus para adicionar a pergunta se o usuário deseja continuar

# Correção

"""
cont = ("zero", "um", "dois", "três", "quatro", 
    "cinco", "seis", "sete", "oito", "nove", 
    "dez", "onze", "doze", "treze", "quatorze", 
    "quinze", "dezesseis", "dezessete", "dezoito", 
    "dezenove", "vinte")

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')
"""