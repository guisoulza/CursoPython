#Tipos Primitivos e Saída de Dados.

n1=int(input('Digite um valor '))
print(type(n1))
n2=int(input('Digite outro valor '))                                                       #pede 2 valores ao usúario.
print(type(n2))
s=n1+n2                                                                                    #Soma dos valores.
#print('A soma entre', n1, 'e', n2, 'é', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))                              #Imprime a soma dos valores.