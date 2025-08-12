#Operadores Aritméticos.

km=float(input('Km percorridos: '))
d=int(input('Dias percorridos: '))
p=d*60+km*0.15
print('Andou {}km por {} dias'.format(km,d))
print('Valor total a pagar: R${:.2f}'.format(p))