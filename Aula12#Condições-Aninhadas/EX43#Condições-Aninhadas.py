#Condições Aninhadas.

#43 - Faça um programa que leia e calcule o IMC:

#18.5: Abaixo do peso;
#18.6 até 24.9: Peso ideal;
#25 até 29.9: Sobrepeso;
#30 até 39.9: Obesidade;
#Acima ou igual a 40: Obesidade mórbida.

altura = float(input('Qual é a sua altura?\n'))
peso = float(input('Qual é a seu peso?\n'))
imc = peso / (altura * altura)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está Obeso!')
elif imc >= 40:
    print('Você está Obeso morbido!')