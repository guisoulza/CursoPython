#Tuplas

#77 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = (
    "computador", "python", "monitor", "teclado", "mouse",
    "cadeira", "janela", "livro", "caneta", "garrafa",
    "mesa", "porta", "telefone", "carro", "caderno"
)

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}', end=', ')