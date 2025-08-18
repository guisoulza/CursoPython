# Aula 14

Nessa aula, é a continuação do estudo dos laços e é mostrado como usar a estrutura de repetição while no Python. Por exemplo:

    c=1
    while c !=10:
        print(c)
        c+=1
    print('Acabou')

# Estrutura de Repetição while em Python.

O while é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira. É útil quando não sabemos exatamente quantas vezes o código deve ser repetido.

Cuidado com loops infinitos

Se a condição nunca ficar falsa, o loop nunca termina! Sempre garanta que a condição será eventualmente falsa.

O while é ótimo para situações onde o número de repetições depende de uma condição dinâmica.

# Exercícios

57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado peça a digitação novamente até ter um valor correto.

58 - Melhore o jogo do exercício 028 onde o computador vai "pensar" em um número de 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

59 - Crie um programa que leia dois valores e mostre um menu ba tela:
* [1] Somar;
* [2] Multiplicar;
* [3] Maior;
* [4] Novos números;
* [5] Sair do programa.

60 - Faça um programa que leia um número qualquer e mostre seu fatorial.

61 - Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progreção utilizando a estrutura while.

62 - Melhore o exercício 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

63 - Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros elementos de uma sequência de Fibonacci.

64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor "999", que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
