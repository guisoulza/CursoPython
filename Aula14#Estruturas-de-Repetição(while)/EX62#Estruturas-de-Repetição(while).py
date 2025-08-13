#Estruturas de repetição(while).

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = n
cont = 1
total = 10                                                      #inicialmente mostra 10 termos
while total != 0:                                               #loop para controlar a PA enquanto o usuário não digitar 0
    fim = cont + total - 1                                      #incrementa o total com a variável fim criada dentro do loop e colocado -1 para não mostrar o 11º termo
    while cont <= fim:                                          #Nesta linha o loop vai parar quando a variável contadora chegar a 10
        print(termo, end=' ')
        termo += r                                              #A variável termo é incrementada com a variável r
        cont += 1                                               #Adiciona +1 a variável contadora para controle do loop
    total = int(input('\nQuantos termos a mais você quer mostrar? (0 para sair) '))

print('Fim da progressão.')


#Correção

"""
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:                                               #loop para controlar a PA enquanto o usuário não digitar 0
    total += mais                                              #incrementa o total com a variável mais que já vale 10
    while cont <= total:                                       #Nesta linha o loop vai parar quando a variável contadora chegar a 10
        print(f'{termo} -> ', end='')
        termo += razao                                         #A variável termo é incrementada com a variável r
        cont += 1                                              #Adiciona +1 a variável contadora para controle do loop
        mais = int(input('Quantos termos você quer mostrar a mais? (0 para sair) '))
    print('PAUSA')
print(f'Progressão finalizada com {total} termos mostrados.')

#A forma corrigida ficou mais completa e legível
"""