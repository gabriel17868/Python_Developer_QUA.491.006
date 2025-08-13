# Declaração de váriaveis
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",", "."))

# Estrutura de decisão
if idade >= 12 and altura >= 1.15:
    print(f"{nome} está autorizado a entrar.")
else:
    print(f"{nome} não está autorizado a entrar")
