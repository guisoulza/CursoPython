#Manipulando Cadeias de Texto.

nome=str(input('Digite seu nome completo: ')).strip()
nome1=nome.replace(' ','')
nome2=nome.split()
print(nome.upper())
print(nome.lower())
print(len(nome1))
print(len(nome2[0]))

print('analisando seu nome...')
print('seu nome em maiusculo é {}'.format(nome.upper()))
print('seu nome em minusculo é {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(len(nome2[0])))