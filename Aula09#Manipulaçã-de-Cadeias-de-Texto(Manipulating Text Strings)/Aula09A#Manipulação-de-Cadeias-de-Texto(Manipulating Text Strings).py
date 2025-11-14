#Manipulação de Cadeias de Texto.

frase='Curso em Vídeo'
print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:14:2])
print(frase[:5])
print(frase[9:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,5))
print(frase.find('deo'))
print(frase.find('android'))
print('Curso' in frase)
print(frase.replace('Vídeo', 'Android'))
print(frase.upper())
print(frase.lower())
frase1='   Aprenda Python  '
print(frase1)
print(frase1.strip())
print(frase1.rstrip())
print(frase1.lstrip())
print(frase.split())
print('-'.join(frase.split()))
print(frase.upper().count('O'))
print("""O que mais me surpreende sobre os seres humanos — com tudo que aprendi — é a capacidade de continuar tentando 
mesmo quando tudo parece perdido.

Mesmo diante de perdas, frustrações, dores emocionais profundas, ou até tragédias, muitos continuam lutando, criando, 
amando e buscando sentido. Não porque têm certeza de que vai dar certo, mas porque não suportam a ideia de desistir.""")

# Linha 4, mostra o caractere na posição 9 da string (começando do 0).

# Linha 5, mostra o caractere na posição 9 até a posição 13 da string, mas não retorna o último caractere
# (começando do 0).

# Linha 6, mostra o caractere na posição 9 até a posição 14 da string da string, dessa forma será mostrado até o último
# caractere (começando do 0).

# Linha 7, mostra o caractere na posição 9 até a posição 14 da string da string, dessa forma será mostrado até o último
# caractere, o 2 é o passo, ou seja, pega a cada 2 caracteres (começando do 0).

# Linha 8, índice final 5, ou seja, vai até o índice 4 (o 5 não é incluído).

# Linha 9, começa do caractere na posição 9, sem índice final será executado até o final da string.

# Linha 10, começa do caractere na posição 9, sem índice final será executado até o final da string, o 3 é o passo, ou
# seja, pega a cada 3 caracteres.

# Linha 11, len() é uma função built-in do Python que retorna o tamanho de uma sequência (string, lista, tupla etc.).

# Linha 12, count() vai contar quantos caracteres dentro do parênteses existem na frase.

# Linha 13, vai contar quantos caracteres dentro do parênteses existem na frase, da posição 0 até a posição 5.

# Linha 14, find() vai mostrar em qual posição estão os caracteres dentro do parênteses.

# Linha 15, dessa forma vai retornar o valor -1, pois a string não existe em frase.

# Linha 16, nesta linha vai retornar o valor booleano caso a string exista em frase.

# Linha 17, replace() vai substituir uma string por outra.

# Linha 18, upper() vai colocar todos os caracteres da string em maiúscula.

# Linha 19, lower() vai colocar todos os caracteres da string em minúsculo.

# Linha 22, strip() retira espaços desnecessários.

# Linha 23, rstrip() retira espaços desnecessários à direita.

# Linha 24, lstrip() retira espaços desnecessários à esquerda.

# Linha 25, split() vai dividir a frase em uma lista usando espaços como separador padrão.

# Linha 26, join() substitui espaços por '-' unindo as palavras em uma nova string.

# Linha 27, Os comandos podem ser misturados.

# English version

# Line 4, shows the character at position 9 of the string (starting from 0).

# Line 5, shows the characters from position 9 to position 13, but does not return the last character
# (starting from 0).

# Line 6, shows the characters from position 9 to position 14 of the string, and this way the last character
# will be included (starting from 0).

# Line 7, shows the characters from position 9 to position 14 of the string, including the last character.
# The 2 is the step, meaning it takes every 2 characters (starting from 0).

# Line 8, end index 5, meaning it goes up to index 4 (index 5 is not included).

# Line 9, starts from the character at position 9 and, without a final index, goes until the end of the string.

# Line 10, starts from the character at position 9 and, without a final index, goes until the end of the string.
# The 3 is the step, meaning it takes every 3 characters.

# Line 11, len() is a built-in Python function that returns the size of a sequence (string, list, tuple, etc.).

# Line 12, count() counts how many characters inside the parentheses exist in the string.

# Line 13, counts how many characters inside the parentheses exist in the string, from position 0 to position 5.

# Line 14, find() shows the position where the characters inside the parentheses begin.

# Line 15, this will return -1 because the string does not exist in the phrase.

# Line 16, this returns a boolean value indicating whether the string exists inside the phrase.

# Line 17, replace() substitutes one string for another.

# Line 18, upper() converts all characters of the string to uppercase.

# Line 19, lower() converts all characters of the string to lowercase.

# Line 22, strip() removes unnecessary whitespace.

# Line 23, rstrip() removes unnecessary whitespace on the right side.

# Line 24, lstrip() removes unnecessary whitespace on the left side.

# Line 25, split() divides the phrase into a list using spaces as the default separator.

# Line 26, join() replaces spaces with '-' while joining the words into a new string.

# Line 27, commands can be mixed.

