#Tuplas

#77 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = (
    "computador", "python", "monitor", "teclado", "mouse",
    "cadeira", "janela", "livro", "caneta", "garrafa",
    "mesa", "porta", "telefone", "carro", "caderno"
)

for p in palavras:
    vogais = ()                                     #Tupla vazia para armazenar vogais
    for letra in p:
        if letra in "aeiou":
            vogais += (letra,)                      #Adiciona vogal à tupla
    print(f'Na palavra {p} temos ', end='')
    print(", ".join(vogais))