#Estruturas de repetição(while).

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = n
cont = 1
total = 10  # inicialmente mostra 10 termos

while total != 0:
    fim = cont + total - 1
    while cont <= fim:
        print(termo, end=' ')
        termo += r
        cont += 1
    total = int(input('\nQuantos termos a mais você quer mostrar? (0 para sair) '))

print('Fim da progressão.')