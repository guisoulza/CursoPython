#Estruturas de repetição(for).

f = str(input('Digite um frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'\nO inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')



'''if f == f[::-1]:
    print('É um palindromo')
else:
    print('Não é um palindromo')'''

#Socorram-me subi no ônibus em Marrocos O lobo ama o bolo