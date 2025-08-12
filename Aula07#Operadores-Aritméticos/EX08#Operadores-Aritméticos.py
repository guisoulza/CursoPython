#Operadores Aritméticos.

t=float(input('Digite o tamanho em metros: '))
km=t*0.001
hm=t*0.010
dam=t*0.100
dm=t*10
cm=t*100
mm=t*1000
print('\033[7m{}m convetido fica: \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm.\n\033[m'.format(t, km, hm, dam, dm, cm, mm))