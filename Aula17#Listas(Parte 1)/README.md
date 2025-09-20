# Aula 17

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# Criando listas

    frutas = ["maçã", "banana", "uva"]
    numeros = [10, 20, 30, 40]
    mistura = ["python", 3.14, True]

Podemos criar listas usando colchetes [], e elas podem armazenar diferentes tipos de dados.

# Acessando elementos

    frutas = ["maçã", "banana", "uva"]
    print(frutas[0])
    print(frutas[-1])

Cada item da lista tem uma posição (índice), começando do 0. Também é possível acessar de trás para frente usando índices negativos.

# Alterando valores

    frutas = ["maçã", "banana", "uva"]
    frutas[1] = "laranja"
    print(frutas)

Como listas são mutáveis, podemos modificar um elemento específico diretamente pelo índice.

# Principais métodos

    frutas = ["maçã", "banana", "uva"]
    frutas.append("pera")
    frutas.insert(1, "kiwi")
    frutas.remove("banana")
    frutas.sort()
    frutas.sort(reverse=True)

Listas possuem métodos úteis para manipulação dos dados:

append() → adiciona ao final.

insert() → insere em uma posição específica.

remove() → remove o primeiro valor correspondente.

sort() → ordena a lista.

sort(reverse=True) → ordena em ordem decrescente.

# Tamanho da lista

    numeros = [5, 8, 12, 20]
    print(len(numeros))

O comando len() mostra quantos elementos existem dentro da lista.

# Laços com listas

    nomes = ["Ana", "Carlos", "João"]
    
    for nome in nomes:
        print(nome)
    
    for indice, nome in enumerate(nomes):
        print(f"Posição {indice}: {nome}")

É comum percorrer listas usando laços for, seja apenas pelos valores ou também pelos índices.

# Cópias de listas

    a = [1, 2, 3]
    b = a[:]
    b[0] = 99
    print(a)
    print(b)

Se atribuirmos uma lista a outra, elas ficam ligadas (qualquer alteração em uma reflete na outra).
Para criar uma cópia independente, usamos fatiamento [:].

# Diferença entre listas e tuplas

Listas -> mutáveis.

Tuplas -> imutáveis.

# Exercícios

78 - Faça um programa que leia 5 valores numéricos e guarde-os em um lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

79 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em um lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

80 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

81 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

* Quantos números foram digitados
* A lista de valores, ordenada de forma decrescente.
* Se o valor 5 foi digitado e está ou não na lista.

82 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

83 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.