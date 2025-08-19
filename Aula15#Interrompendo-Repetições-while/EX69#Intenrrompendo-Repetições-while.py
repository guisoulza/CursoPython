#Interrompendo Repetições while.

#69 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar ou não continuar. No final mostre:
#* Quantos tem mais de 18;
#* Quantos homens foram cadastrados;
#* Quantas mulheres tem menos de 20 anos.

cm = cf = ci = 0
print('-' * 20)
while True:
    idade = int(input('Idade: '))
    genero = str(input('Genero [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        ci += 1
    if genero == 'M':
        cm += 1
    if genero == 'F' and idade < 20:
        cf += 1
    adiante = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if adiante not in 'SN':
        print('Opção inválida! Digite novamente.')
        adiante = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if adiante == 'N':
        break
    print('-' * 20)
print(f'Tem {ci} pessoas acima de 18, {cm} homens, e {cf} mulheres com menos de 20 anos.')