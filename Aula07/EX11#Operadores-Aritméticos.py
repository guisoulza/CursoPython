#Operadores Aritméticos.

a=float(input('Digite a altura: '))
l=float(input('Digite a largura: '))
m=a*l
t=m/2
print('\033[7mSua parede tem a dimenção de {}x{} e sua area é de {}m²\033[m'.format(a,l,m))
print('\033[7mVai precisar de {} litros de tinta para pintar {}m² da parede\033[m'.format(t,m))