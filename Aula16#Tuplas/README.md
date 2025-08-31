# Aula 16

Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# Criando tuplas

    #Tupla comum
    tupla = (10, 20, 30)

    #Tupla com diferentes tipos
    tupla2 = (1, "texto", 3.14, True)

    #Tupla com apenas um elemento (precisa da vírgula no final)
    tupla3 = (5,)

Sempre use parênteses () para criar tuplas.

Acessando elementos:

    valores = (10, 20, 30, 40)
    print(valores[0])   #10
    print(valores[-1])  #40


Dá pra acessar pelo índice.

Métodos úteis:

    numeros = (1, 2, 2, 3, 4)
    print(numeros.count(2))  #2 → conta quantas vezes aparece
    print(numeros.index(3))  #3 → mostra a posição do elemento

As tuplas têm poucos métodos, mas esses dois ajudam bastante.

Desempacotando tuplas:

    ponto = (4, 5)
    x, y = ponto
    print(x)  # 4
    print(y)  # 5

Você pode desmontar uma tupla em várias variáveis de uma vez.

Tuplas com estrutura de repetição:

    for c in numeros:
        print(c)  #1, 2, 2, 3, 4 → mostra os valores que estão na tupla utilizando a variável "c" da estrutura de repetição.

Podemos utilizar estruturas de repetição com as tuplas.

Tuplas são imutáveis, ou seja, quando quiser armazenar valores fixos que não podem ser alterados (ex.: coordenadas, dias da semana).

# Exercícios

72 - Crie um programa que tenha uma tupla totalmente preenchida por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por exteso.

73 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

* Apenas os 5 primeiros colocados.
* Os últimos 4 colocados da tabela.
* Uma lista com os times em ordem alfabética.
* Em que posição na tabela está o time Chapecoence.

74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

* Quantas vezes apareceu o número 9.
* Em que posição foi digitado o primeiro valor 3.
* Quais foram o números pares.

76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular. 
 
77 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais vogais são as suas vogais.