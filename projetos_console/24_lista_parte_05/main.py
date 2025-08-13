# lista
itens = [
    "Chocolate",
    "Feijão",
    "Arroz",
    "Macarrão",
    "Biscoito",
    "Ovos",
    "Leite",
    "Frango"
]

# Exibe a lista de campras
itens[i] = input("Informe o novo valor: ").capitalize().strip()

# Usuário informa o índice a ser alterado
try:
    i = int(input("Informe a posição do índice a ser alterado: "))
    if i >= 0 and i < len(itens):
        itens[i] = input("Informe o novo valor: ").capitalize().strip()
        print("Item alterado com sucesso!")
    else:
        print("Índice inválido.")
except Exception as e:
    print(f"Não foi possível alterar o item da lista. {e}.")
finally:
    for i in range(len(itens)):
        print(f"Índice {i}: {itens[i]}.")