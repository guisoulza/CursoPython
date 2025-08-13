#Estruturas de repetição(while).

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
texto = ''                                                              #Variavel de controle do loop
while texto not in ('1', '2', '3', '5'):
    print('-=-' * 10)
    print('Menu rapido:\n\n'
          '[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] sair do programa\n')
    texto = str(input('Como proceder: '))
    if texto == '1':                                                    #Condição de soma
        soma = n1 + n2
        print(f'\nA soma {n1} + {n2} = {soma}')
        print('-=-' * 10)
    elif texto == '2':
        multiplica = n1 * n2                                            #Condição de multiplicação
        print(f'\nA multiplicação {n1} x {n2} = {multiplica}')
        print('-=-' * 10)
    elif texto == '3':                                                  #Condição de que verifica o maior valor digitado
        maior = max(n1, n2)                                             #O max() verifica qual é o maior em todos os valores dentro do parentêses
        print(f'\nO maior número é {maior}')
        print('-=-' * 10)
    elif texto == '4':                                                  #Condição para digitar novamente
        print('Digite novamente...')
        print('-=-' * 10)
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif texto == '5':                                                  #Condição de saída do menú
        print('\nLogout feito com sucesso!')
        print('-=-' * 10)
    else:                                                               #Condição para caso seja digitado alguma opção que não foi solicitada
        print('\nOpção invalida!')
print('Fim')

#Correção

"""
from time import sleep                                                  #Professor adicionou esse modúlo para deixar mais dinâmico
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção?\n'))
    if opcao == 1:                                                      # Condição de soma
        soma = n1 + n2
        print(f'\nSoma: {n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplica = n1 * n2                                            # Condição de multiplicação
        print(f'\n Multiplicação: {n1} x {n2} = {multiplica}')
    elif opcao == 3:                                                    # Condição de que verifica o maior valor digitado
        maior = max(n1, n2)                                             # O max() verifica qual é o maior em todos os valores dentro do parentêses
        print(f'\nO maior número é {maior}')
    elif opcao == 4:                                                    # Condição para digitar novamente
        print('Digite novamente...\n')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:                                                    # Condição de saída do menú
        print('Logout feito com sucesso!')
    else:                                                               # Condição para caso seja digitado alguma opção que não foi solicitada
        print('\nOpção invalida!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa, Volte sempre!!!')
"""
