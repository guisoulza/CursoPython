#Tuplas

#73 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabética.
# Em que posição na tabela está o time Chapecoence.

classificacao = (
    "Goiás", "Coritiba", "Novorizontino", "Chapecoense", "Remo",
    "Avaí", "Cuiabá", "Criciúma", "Vila Nova", "Atlético-GO",
    "Operário-PR", "Athletico Paranaense", "Ferroviária", "CRB", "Athletic-MG",
    "Volta Redonda", "América-MG", "Botafogo-SP", "Paysandu", "Amazonas FC"
)

print(f'{'Brasileirão série B':^30}')
print('-' * 230)
print(f'Os 5 primeiros colocados são:\n{', '.join(classificacao[:5])}')                                     #join() é uma forma de mostrar o resultado de uma variável composta sem a poluição das aspas e dos parentêses, conchete ou chaves.
print('-' * 230)
print(f'Os 4 últimos colocados são:\n{', '.join(classificacao[-4:])}')
print('-' * 230)
print(f"A ordem alfabética é: \n{(', '.join(sorted(classificacao)))}")
print('-' * 230)
print(f'Chapecoense esta na posição: {classificacao.index('Chapecoense') + 1}º')
print('-' * 230)