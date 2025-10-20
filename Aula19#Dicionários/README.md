# Aula 19

Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis 
compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

## Dicionários em python

Dicionários são representados por {}.

* Em listas e tuplas, os dados são contabilizados a partir do zero (0), já no dicionário podemos dar nome aos dados.

        dados = dict()
        dados = {'nome': 'Pedro', 'idade': 25}
        
        print(dados['nome'])   --> Pedro
        print(dados['idade'])  --> 25

* O append() não funciona com dicionários, mas podemos adicionar novos elementos assim:

        dados['sexo'] = 'M'

* Para eliminar elementos, usamos del:

        del dados['idade']


## Exemplo prático:

        filme = {"titulo": "Star Wars", "ano": 1977, "diretor": "George Lucas"}


* Usando o método values(), serão mostrados apenas os valores do dicionário:

        print(filme.values())


* Para mostrar as chaves, usamos keys():

        print(filme.keys())


* Para mostrar chaves e valores juntos, usamos items():

        print(filme.items())

* Para percorrer o dicionário mostrando chaves e valores em ordem:

        for k, v in filme.items():
            print(f'O {k} é {v}')


Também é possível criar dicionários dentro de listas.

## Exemplo prático — simulando uma locadora:

        filme1 = {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}
        filme2 = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
        filme3 = {'titulo': 'Vingadores', 'ano': 2012, 'diretor': 'Joss Whedon'}
        
        locadora = [filme1, filme2, filme3]
        
        print(locadora[0]['ano'])     # --> 1999
        print(locadora[1]['titulo'])  # --> Star Wars


* O fatiamento com [:] não funciona em dicionários. Em vez disso, usamos o método copy() para duplicar corretamente:

        locadora.append(filme.copy())


## Exercícios

90 - Faça um programa que leia nome e média de um aluno, guardando tambem a situação em um dicionário. No final mostre 
o conteúdo da estrutura na tela.

91 - Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados em um 
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um 
dicionário se por acaso a CTPS for diferente de 0, o dicionário receberá tambem o ano de contratação e o salário.
Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.

93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
guardado em um dicionário incluindo o total de gols feitos durante o campeonato.

94 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando cada pessoa em um dicionário e todos os 
dicionários em uma lista. No final mostre:

* Quantas pessoas foram cadastradas.
* A média de idade do grupo.
* Uma lista com todas as mulheres.
* Uma lista com todas as pessoas com idade acima da média.

95 - Aprimore o exercício 93 para que ele funcione com vários jogadores incluindo um sistema de visualização de 
detalhes do aproveitamento de cada jogador.