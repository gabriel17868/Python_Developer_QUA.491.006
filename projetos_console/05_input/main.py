#Entrada de dados.
nome = input("Informe seu nome: ")
idade = int(input("Informe a sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",", ".")) #.replace vai substituí a virgula por ponto caso seja utilizado.

#Saída de dados.
print(f"Seja bem vindo ao curso de python, {nome}!")
print(f"Idade do usuário: {idade}.")
print(f"Altura do usuário: {altura}.")

#Verificando o tipo de dados.
print(f"{nome}: {type(nome)}.")
print(f"{idade}: {type(idade)}.") 
print(f"{altura}: {type(altura)}")      