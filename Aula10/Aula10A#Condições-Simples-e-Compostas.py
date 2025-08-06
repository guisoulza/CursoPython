

nome = str(input('Digite seu nome: '))
if nome == 'Guilherme':
     print('Seu nome é bem grande em!!')
else:
     print('Seu nome é bem normal!!')
print('Bom dia, {}'.format(nome))

n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
if m >= 5:
    print('Passou!')
else:
    print('Reprovado!')
print('Sua nota foi {}'.format(m))