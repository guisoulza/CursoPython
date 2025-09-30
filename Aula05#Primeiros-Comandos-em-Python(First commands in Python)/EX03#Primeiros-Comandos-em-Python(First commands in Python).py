# Primeiros Comandos em python (First commands in Python).

# 03 - Crie um script que leia dois números e mostre a soma entre eles.
# 03 - Create a script that reads two numbers and displays their sum.

n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s = n1+n2                                           # Nesta linha a variável "s" será a soma de "n1" e "n2".
                                                    # In this line, the variable "s" will be the sum of "n1" and "n2".
print('A soma de \033[34m{}\033[m e \033[34m{}\033[m é igual a \033[32m{}\033[m'.format(n1, n2, s))