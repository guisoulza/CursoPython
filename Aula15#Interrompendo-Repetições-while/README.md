# Aula 15

Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho. Por exemplo:

    c = 1
    while c <= 10:
        if c == 5:
            break
        print(c)
        c += 1
    print("Fim do loop")

# O comando break em Python

O break é utilizado para forçar a saída imediata de um loop, mesmo que a condição ainda seja verdadeira.
Isso é útil quando queremos parar a repetição assim que uma determinada condição for atendida.

Cuidado ao usar o break

* Se usado sem planejamento, pode interromper o loop em momentos indesejados.

* É importante pensar em qual situação o laço deve parar antes de inserir o break.

O break é muito útil quando a repetição precisa ser encerrada assim que um evento acontecer, sem esperar o término natural do laço.

# Exercícios

66 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor "999", que é a condição de parada. No final, mostre quantos números foram digitado e qual foi a soma entre eles (desconsiderando o flag).

67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. o programa será interrompido quando o número solicitado for negativo.

68 - Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

69 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar ou não continuar. No final mostre:

* Quantos tem mais de 18;
* Quantos homens foram cadastrados;
* Quantas mulheres tem menos de 20 anos.

70 - Crie um programa que leia o nome e o preço de vários produtos. O Programa deverá perguntar se o usuário vai continuar. No final mostre:

* Total gasto na compra;
* Quantos produtos custam mais de R$1000;
* Qual produto mais barato.

71 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual valor será sacado (número inteiro) e o programa deve informar quantas cédulas de cada valor serão entregues. OBS: Caixa possui notas de 50, 20, 10 e 1.
