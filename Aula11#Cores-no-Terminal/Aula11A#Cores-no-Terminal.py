#Cores no Terminal.

print('Olá, Mundo!!\033[m')

a= 5
b= 3
print('Os valores são \33[32m{}\33[m e \33[31m{}\33[m e \33[m'.format(a,b))

nome = 'Gui'
print('Prazer {}{}{}'.format('\033[4;34m',nome, '\033[m'))

cores = {'limpa' : '\033[m',
         'azul ;' : '\033[34,',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[34m'}
