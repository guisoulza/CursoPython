#Condições Simples e Compostas.

#31 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 pra viagens mais longas.

d = int(input('Digite a distancia: '))
v = float(d * 0.50)
v1 = float(d * 0.45)
if d <= 200:
    print('Sua viagem de {}Km vai estar no valor de R${:.2f}'.format(d, v))
else:
    print('Sua viagem de {}Km vai estar no valor de R${:.2f}'.format(d, v1))