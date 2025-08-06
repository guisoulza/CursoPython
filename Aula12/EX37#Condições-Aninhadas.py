#Condições Aninhadas.

num = int(input('Qual o numero?\n'))
print('1 para binario\n2 para octal\n3 para hexadecimal')
escolhanum = int(input('Qual a base de conversão você deseja?\n'))
if escolhanum == 1:
    print(bin(num)[2:])
elif escolhanum == 2:
    print(oct(num)[2:])
elif escolhanum == 3:
    print(hex(num)[2:])
else:
    print('\033[31mErro!\033[m')