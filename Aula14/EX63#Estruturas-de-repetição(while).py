#Estruturas de repetição(while).

n = int(input('Digite quantos numeros vão para a sequencia: '))
antigo = 0
novo = 1
seq = 0
c = 1

while c <= n:
    print(seq, end=' ')
    seq = novo + antigo
    antigo = novo
    novo = seq
    c += 1
