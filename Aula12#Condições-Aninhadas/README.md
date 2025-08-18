# Aula 12

Nessa aula, é mostrado como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

# Condições Aninhadas em Python
As condições aninhadas são estruturas if dentro de outras estruturas if. Elas são usadas quando precisamos verificar mais de uma condição em níveis diferentes de decisão.

    idade = 20
    tem_carteira = True
    
    if idade >= 18:
        if tem_carteira:
            print("Pode dirigir.")
        else:
            print("É maior de idade, mas não tem carteira.")
    else:
        print("Não pode dirigir.")
Dica: Embora condições aninhadas sejam úteis, evite exagerar, pois podem deixar o código mais difícil de ler. Em muitos casos, pode usar operadores lógicos (and, or) para simplificar.

# Exercícios

36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comproador e em quantos anos ele pretende pagar. Calcule o valor da prestação sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

37 - Escreva um programa que leia um número inteiro qualquer  e peça para o usuário escolher qual será a base de conversão:

* 1 para binário;
* 2 para octal;
* 3 para hexadecimal.

38 - Escreva um programa que leia dois números inteiros e compare-os mostrando na tela um mensagem:

* O primeiro valor é maior;
* O segundo valor é menor;
* Os 2 valores são iguais.

39 - Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:

* Se ele ainda vai se alistar ao serviço militar;
* Se é a hora de se alistar;
* Se já passou do tempo de alistamento.

40 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

* Média abaixo de 5.0 -> Reprovado;
* Média entre 5.0 e 6.9 -> Recuperação;
* Média 7.0 ou superior -> Aprovado.

41 - A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

* Até 9 anos: Mirim;
* Até 14 anos: Infantil;
* Até 19 anos: Junior;
* Até 20 anos: Sênior;
* Acima: Master.

42 - Refaça o Exercício 035 dos triângulos, acrescentando o tipo de triângulo será formado:

* Equilátero: Lados iguais;
* Isósceles: 2 lados iguais;
* Escaleno: Lados diferentes.

43 - Faça um programa que leia e calcule o IMC:

* 18.5: Abaixo do peso;
* 18.6 até 24.9: Peso ideal;
* 25 até 29.9: Sobrepeso;
* 30 até 39.9: Obesidade;
* Acima ou igual a 40: Obesidade mórbida.

44 - Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento:

* A vista: 10% de desconto;
* Cartão a vista: 5% de desconto;
* parcelado em 2x: preço normal;
* parcelado em 3x ou mais: 20% de juros.

45 - Faça um JOKENPO.
