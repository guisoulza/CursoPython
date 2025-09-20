# Listas(Parte 2)

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que 
permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

## Recapitulando Listas em Python

### Criando uma lista

    dados = list()            # Declara 'dados' como lista
    dados.append('Pedro')     # Adiciona 'Pedro' à lista
    dados.append(25)          # Adiciona 25 à lista
    
    print(dados[0])  # imprime 'Pedro'
    print(dados[1])  # imprime 25

### Listas dentro de listas

    pessoas = list()
    pessoas.append(dados[:])  # Copia a lista 'dados' dentro de 'pessoas'

Agora, pessoas é uma lista de listas. Isso permite organizar informações em forma de tabela, por exemplo.

Forma prática de declarar listas de listas:

    pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

Aqui, cada item da lista principal é outra lista, contendo nome e idade.

### Acessando valores em listas dentro de listas

Use dois colchetes para acessar elementos específicos:

    print(pessoas[0][0])  # imprime 'Pedro'
    print(pessoas[1][1])  # imprime 19
    print(pessoas[2][0])  # imprime 'João'
    print(pessoas[2])     # imprime ['João', 32]

O primeiro índice ([0], [1], [2]...) escolhe a pessoa.
O segundo índice ([0], [1]) escolhe o dado dentro da pessoa (nome ou idade).

# Exercícios

84 - Faça um programa que leia nome e peso de várias pessoas, guardadndo tudo em uma lista. No final mostre:

* Quantas pessoas foram cadastradas.
* Uma listagem com as pessoas mais pesadas(+100kg).
* Uma listagem com as pessoas mais leves(-70kg).

85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha 
separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.

86 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a
matriz na tela, com a formatação correta.

87 - Aprimore o desafio anterior, mostrando no final:

* A soma de todos os valores pares digitados.
* A soma dos valores da terceira coluna.
* O maior valor da segunda linha.

88 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre 
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.