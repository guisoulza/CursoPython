#Condições Aninhadas.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Sua média é de {} e você está reprovado'.format(media))
elif media < 6.9:
    print('Sua média é de {} e você está de recuperação'.format(media))
elif media >= 7.0:
    print('Sua média é de {} e você está aprovado'.format(media))