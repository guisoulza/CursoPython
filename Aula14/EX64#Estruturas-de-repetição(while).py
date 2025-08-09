c = 0
soma = 0
n = int(input('Digite um valor (999 para parar): '))

while n != 999:
        soma = soma + n
        n = int(input('Digite um valor (999 para parar): '))
        c += 1

print(f'Foram digitados {c} números e a soma dos valores é {soma}')



