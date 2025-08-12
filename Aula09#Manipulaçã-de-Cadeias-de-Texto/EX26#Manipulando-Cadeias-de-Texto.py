#Manipulando Cadeias de Texto.

frase=str(input('Digite a frase: ')).strip().upper()
print(frase.count('A'))
print(frase.find('A')+1)
print(frase.rfind('A')+1)
