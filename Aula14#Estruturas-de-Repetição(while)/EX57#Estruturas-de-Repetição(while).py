#Estruturas de repetição(while).

#57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado peça a digitação novamente até ter um valor correto.

genero = ""                                                                #Variável para controle do loop
while genero not in ('M', 'F'):                                            #Nesta linha o loop vai continuar enquanto o usuário não digitar o que foi solicitado
    genero = input('Digite o seu gênero ( M / F ): ').upper().strip()[0]
    if genero == 'M':                                                      #Condição para quando a variável genero se igualar a M
        print('Seu gênero é masculino')
    elif genero == 'F':                                                    #Condição para quando a variável genero se igualar a F
        print('Seu gênero é feminino')
    else:                                                                  #Condição para caso o usuário digitar algo que não foi solicitado
        print('Gênero não identificado digite novamente.')
print('Gênero salvo com sucesso!')


#Correção

"""
genero = str(input('Digite seu sexo [ M / F]: ')).upper().strip()[0]
while genero not in 'MmFf':                                                #Loop para caso o usuário digitar algo que não foi solicitado
    genero = str(input('Opção invalida, por favor digite seu sexo [ M / F]: ')).upper().strip()[0]
print(f'Seu gênero {genero} foi registrado com sucesso!!')

#Por mais que essa seja a resposta do professor, creio que a minha resposta está mais completa.

"""