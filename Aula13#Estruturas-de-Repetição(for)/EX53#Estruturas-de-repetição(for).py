#Estruturas de repetição(for).

#53 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

f = str(input('Digite um frase: ')).strip().upper()             #Recebe a frase do usuário, remove espaços extras e converte para maiúsculas.
palavras = f.split()                                            #Divide a frase em palavras (para remover espaços entre elas).
junto = ''.join(palavras)                                       #Junta as palavras em uma única string, sem espaços.
inverso = ''                                                    #Inicializa a variável que vai armazenar o inverso da string.
for letra in range(len(junto)-1, -1, -1):                       #Loop para percorrer a string de trás para frente e construir o inverso.
    inverso += junto[letra]
print(f'\nO inverso de {junto} é {inverso}')
if inverso == junto:                                            #Verifica se a frase é igual ao seu inverso
    print('É um palindromo')
else:
    print('Não é um palindromo')



'''if f == f[::-1]:
    print('É um palindromo')
else:
    print('Não é um palindromo')'''

#Socorram-me subi no ônibus em Marrocos, O lobo ama o bolo