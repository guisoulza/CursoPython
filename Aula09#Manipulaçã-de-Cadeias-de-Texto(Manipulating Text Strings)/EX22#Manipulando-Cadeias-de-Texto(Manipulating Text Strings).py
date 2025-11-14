# Manipulando Cadeias de Texto (Manipulating Text Strings).

# 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# Quantas letras ao total (Sem considerar espaços);
# Quantas letras tem o primeiro nome;

# 22 - Create a program that reads a person's full name and displays:

# The name with all letters in uppercase;
# The name with all letters in lowercase;
# How many letters in total (not counting spaces);
# How many letters are in the first name;

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