# Operadores Aritiméticos (Arithmetic Operators).

nome=input('Qual o seu nome? ')
print('Prazer {:=^20}!'.format(nome))
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s=n1+n2         # Adição (Addition).
s1= n1-n2       # Subtração (Subtraction).
m=n1*n2         # Multiplicação (Multiplication).
d=n1/n2         # Divisão (Division).
d1=n1//n2       # Divisão inteira ou truncada (Integer or floor division).
e=n1**n2        # Exponenciação (Exponentiation).
print('A soma vale {} e a subtração vale {} \n o produto vale {} e a divisão vale {:.3f}'.format(s, s1, m, d), end=' ')
print('Divisão inteira vale {} e potência vale {}'.format(d1, e))
