genero = ""
while genero != 'M' and genero != 'F':
    genero = input('Digite o seu genero ( M / F ): ').upper().strip()
    if genero == 'M':
        print('Seu gênero é masculino')
    elif genero == 'F':
        print('Seu genero é feminino')
    else:
        print('Genero não identificado digite novamente')
print('Fim')