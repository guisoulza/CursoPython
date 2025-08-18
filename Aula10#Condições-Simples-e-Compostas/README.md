# Aula 10
Nessa aula, será mostrado como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

Condições Simples e Compostas em Python
Em Python, usamos estruturas condicionais para tomar decisões com base em testes lógicos. Elas permitem que o programa execute diferentes blocos de código dependendo das condições especificadas.

# Condição Simples (if)
    idade = 18
    if idade >= 18:
      print("Você é maior de idade.")
Nesse exemplo, o print só será executado se a condição idade >= 18 for verdadeira.

# Condições Compostas (Operadores Lógicos)
    and → todas as condições precisam ser verdadeiras
    
    or → pelo menos uma condição precisa ser verdadeira
    
    not → inverte o valor lógico

# Operadores Relacionais
    Operador    Significado
    ==          Igual 
    !=          Diferente
    >           Maior 
    <           Menor 
    =>          Maior ou igual 
    <=          Menor ou igual

Exemplo do uso dos operadores combinados:

    idade = 20
    tem_carteira = True

    if idade >= 18 and tem_carteira:
    print("Pode dirigir.")

# Exercícios

28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual o número escolhido pelo computador. O programa deve dizer se venceu ou perdeu.

29 - Escreva um programa que leia a velocidade de um carro. Se passar de 80km/h mostre que foi multado. A multa vai custar R$7,00 por cada km/h acima do limite.

30 - Crie um programa que se o número é impar ou par.

31 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 pra viagens mais longas.

32 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

33 - Faça um programa que leia 3 números e mostre qual é maior e qual é menor.

34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%. Para inferiores ou iguais o aumento é de 15%.

35 - Desenvolva um programa que leia o comprimento de 3 rotas e diga se podem ou não formar um triângulo.

