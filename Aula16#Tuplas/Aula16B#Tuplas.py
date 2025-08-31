a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a               #Nesse caso a variável "c" virou uma tupla, e a ordem dos fatores na variável "c" vai alterar a ordem da tupla.
"""
c = a + b              #Vai colocar a tupla a antes da tupla b.
"""
print(c)
print(c.count(5))        #Quantas vezes o número 5 ta aparecendo dentro da tupla c.
print(c.index(8))        #Mostra a posição do número 8
print(c.index(2))        #Mostra a posição do número 2, sempre mostrando a primeira ocorrência.