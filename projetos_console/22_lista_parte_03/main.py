# Lista
cidades = [
    "Brasília",
    "São Paulo",
    "Rio de Janeiro",
    "Teresina",
    "Belo Horizinte",
    "Palmas"
]

# Exibe a lista e seus respectivos índices
for i in range(len(cidades)):
    print(f"Índice {i}: {cidades[i]}.")

# Tratamento de exceção
try:
    # Usuário informa o nome da nova cidade e a posição (índice)
    nova_cidade = input("Informe o nome da nova cidade: ").title().strip()
    i = int(input("Informe a posição da lista onde deseja inserir: "))

    if i >= 0 and i <= len(cidades):
        # Insere novo item em uma posição na lista
        cidades.insert(i, nova_cidade)
        print("Cidade inserida com sucesso!")
    else:
        print("Índice inválido.")
except Exception as e:
    print(f"Não foi possível inserir item na lista. {e}.") 
finally:
    # Re-exibe a lista e suas posições
    for i in range(len(cidades)):
        print(f"Índice {i}: {cidades[i]}.")