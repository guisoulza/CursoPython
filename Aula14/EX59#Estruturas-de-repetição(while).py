#Estruturas de repetição(while).

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
texto = ''
while texto not in ('1', '2', '3', '5'):
    print('Menu rapido:\n\n'
          '[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] sair do programa\n')
    texto = str(input('Como proceder: '))
    if texto == '1':
        soma = n1 + n2
        print(f'\nA soma entre {n1} e {n2} é {soma}\n')
    elif texto == '2':
        multiplica = n1 * n2
        print(f'\nA multiplicação entre {n1} e {n2} é {multiplica}\n')
    elif texto == '3':
        maior = max(n1, n2)
        print(f'\nO maior número é {maior}\n')
    elif texto == '4':
        print('\nDigite novamente...\n')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif texto == '5':
        print('\nLogout feito com sucesso!\n')
    else:
        print('\nOpção invalida!\n')
print('Fim')
