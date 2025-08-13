nomes = [
    "Alex",
    "Joana",
    "João",
    "Mariana",
    "Mário",
    "Fernanda"
]

# Exibe a lista
for nome in nomes:
    print(nome)

# Usuário informa nome a ser acrescentado na lista
novo_nome = input("Informe o novo nome: ").title().strip()

# Novo nome é inserido na lista
nomes.append(novo_nome)

# Re-exibe a lista
for nome in nomes:
    print(nome)