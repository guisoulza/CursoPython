teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 19
galera.append(teste[:])
print(teste)

#Não esquecer de realizar a copia com [:] se não ele vai duplicar os valores na lista galera