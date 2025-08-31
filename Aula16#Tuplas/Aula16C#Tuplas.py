pessoa = ('Guilherme', 25, 'M', 80.05)
del(pessoa)                                     #O del() apaga a variável da memória, seja ela simples ou composta.
"""
del(pessoa[1])                                  #Como tuplas são imutaveis, dessa forma o uso do del() será obsoleto.
"""
print(pessoa)                                   #Vai gerar um erro, pois a tupla foi apagada.

