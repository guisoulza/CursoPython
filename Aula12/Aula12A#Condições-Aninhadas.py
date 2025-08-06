#Condições Aninhadas.

nome=str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome Feminino')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}'.format(nome))