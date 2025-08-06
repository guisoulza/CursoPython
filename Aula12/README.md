# Aula12
Nessa aula, é mostrado como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

# Condições Aninhadas em Python
As condições aninhadas são estruturas if dentro de outras estruturas if. Elas são usadas quando precisamos verificar mais de uma condição em níveis diferentes de decisão.

    idade = 20
    tem_carteira = True
    
    if idade >= 18:
        if tem_carteira:
            print("Pode dirigir.")
        else:
            print("É maior de idade, mas não tem carteira.")
    else:
        print("Não pode dirigir.")

Dica:
Embora condições aninhadas sejam úteis, evite exagerar, pois podem deixar o código mais difícil de ler. Em muitos casos, pode usar operadores lógicos (and, or) para simplificar.
