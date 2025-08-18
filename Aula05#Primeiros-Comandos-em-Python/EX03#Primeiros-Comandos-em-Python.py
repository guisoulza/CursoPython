#Primeiros Comandos em python.

#03 - Crie um script que leia dois números e mostre a soma entre eles.

n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s = n1+n2                                               #Nesta linha a variável "s" será a soma de "n1" e "n2".
print('A soma de \033[34m{}\033[m e \033[34m{}\033[m é igual a \033[32m{}\033[m'.format(n1, n2, s))