#Condições Aninhadas.

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