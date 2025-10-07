# Tipos Primitivos e Saída de Dados (Primitive Types and Data Output).

n1=int(input('Digite um valor '))
print(type(n1))                                                 # Pede 2 valores ao usúario (Ask the user for 2 values).
n2=int(input('Digite outro valor '))
print(type(n2))
s=n1+n2                                                                              # Soma dos valores (Sum of values).
"""
print('A soma entre', n1, 'e', n2, 'é', s)
"""
print('A soma entre {} e {} vale {}'.format(n1, n2, s))     # Imprime a soma dos valores (Show the sum of values).