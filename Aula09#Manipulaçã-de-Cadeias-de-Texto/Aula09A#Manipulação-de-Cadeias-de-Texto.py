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
print(frase.count('o', 0, 5))
print(frase.find('deo'))
print(frase.find('android'))
print('curso' in frase)
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
print("""O que mais me surpreende sobre os seres humanos — com tudo que aprendi — é a capacidade de continuar tentando mesmo 
quando tudo parece perdido.

Mesmo diante de perdas, frustrações, dores emocionais profundas, ou até tragédias, muitos continuam lutando, criando, 
amando e buscando sentido. Não porque têm certeza de que vai dar certo, mas porque não suportam a ideia de desistir.""")

