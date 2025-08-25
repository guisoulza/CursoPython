#Manipulação de Cadeias de Texto.

frase='Curso em Vídeo'
print(frase[9])                                             #Mostra o caractere na posição 9 da string (começando do 0).
print(frase[9:13])                                          #Mostra o caractere na posição 9 até a posição 13 da string, mas não retorna o último caractere (começando do 0).
print(frase[9:14])                                          #Mostra o caractere na posição 9 até a posição 14 da string da string, dessa forma será mostrado até o último caractere (começando do 0).
print(frase[9:14:2])                                        #Mostra o caractere na posição 9 até a posição 14 da string da string, dessa forma será mostrado até o último caractere, o 2 é o passo, ou seja, pega a cada 2 caracteres (começando do 0).
print(frase[:5])                                            #Índice final 5, ou seja, vai até o índice 4 (o 5 não é incluído)
print(frase[9:])                                            #Começa do caractere na posição 9, sem índice final será executado até o final da string.
print(frase[9::3])                                          #Começa do caractere na posição 9, sem índice final será executado até o final da string, o 3 é o passo, ou seja, pega a cada 3 caracteres.
print(len(frase))                                           #len() é uma função built-in do Python que retorna o tamanho de uma sequência (string, lista, tupla etc.).
print(frase.count('o'))                                     #count() vai contar quantos caracteres dentro do parentêses existem na frase.
print(frase.count('o',0,5))                 #Vai contar quantos caracteres dentro do parentêses existem na frase, da posição 0 até a posição 5.
print(frase.find('deo'))                                    #find() vai mostrar em qual posição está os caracteres dentro do parentêses.
print(frase.find('android'))                                #Dessa forma vai retornar o valor -1, pois a string não existe em frase.
print('Curso' in frase)                                     #Nesta linha vai retornar o valor booleano caso a string exista em frase.
print(frase.replace('Vídeo', 'Android'))        #replace() vai substituir uma string por outra.
print(frase.upper())                                        #Upper() vai colocar todos os caracteres da string em maiúscula.
print(frase.lower())                                        #Lower() vai colocar todos os caracteres da string em minúsculo.
frase1='   Aprenda Python  '
print(frase1)
print(frase1.strip())                                       #strip() retira espaços desnecessários.
print(frase1.rstrip())                                      #rstrip() retira espaços desnecessários a direita.
print(frase1.lstrip())                                      #lstrip() retira espaços desnecessários a esquerda.
print(frase.split())                                        #split() vai dividir a frase em uma lista usando espaços como separador padrão.
print('-'.join(frase.split()))                              #join() substitui espaços por '-' unindo as palavras em uma nova string.
print(frase.upper().count('O'))                             #Os comando podem ser misturados.
print("""O que mais me surpreende sobre os seres humanos — com tudo que aprendi — é a capacidade de continuar tentando mesmo 
quando tudo parece perdido.

Mesmo diante de perdas, frustrações, dores emocionais profundas, ou até tragédias, muitos continuam lutando, criando, 
amando e buscando sentido. Não porque têm certeza de que vai dar certo, mas porque não suportam a ideia de desistir.""")

