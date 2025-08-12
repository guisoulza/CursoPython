#Condições Simples e Compostas.

d = int(input('Digite a distancia: '))
v = float(d * 0.50)
v1 = float(d * 0.45)
if d <= 200:
    print('Sua viagem de {}Km vai estar no valor de R${:.2f}'.format(d, v))
else:
    print('Sua viagem de {}Km vai estar no valor de R${:.2f}'.format(d, v1))