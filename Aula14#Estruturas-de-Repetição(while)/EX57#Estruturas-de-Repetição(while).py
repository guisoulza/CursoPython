#Estruturas de repetição(while).

"""
genero = ""
while genero not in ('M', 'F'):
    genero = input('Digite o seu genero ( M / F ): ').upper().strip()[0]
    if genero == 'M':
        print('Seu gênero é masculino')
    elif genero == 'F':
        print('Seu genero é feminino')
    else:
        print('Genero não identificado digite novamente')
print('Fim')
"""

#Correção

genero = str(input('Digite seu sexo [ M / F]: ')).upper().strip()[0]
while genero not in 'MmFf':
    genero = str(input('Opção invalida, por favor digite seu sexo [ M / F]: ')).upper().strip()[0]
print(f'Seu genero {genero} foi registrado com sucesso!!')

#Por mais que essa seja a resposta do professor, creio que a minha resposta está mais completa