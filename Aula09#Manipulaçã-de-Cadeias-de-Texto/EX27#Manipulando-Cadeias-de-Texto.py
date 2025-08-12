#Manipulando Cadeias de Texto.

nome = str(input('Digite seu nome: ')).strip()
nome1=nome.split()
print('\033[4;34mO nome {} tem primeiro nome {} e ultimo nome {}\033[m'.format(nome, nome1[0], nome1[-1]))