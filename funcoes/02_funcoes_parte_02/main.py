# Função
def mostrar_msg(nome):
    return f"Seja bem vindo, {nome}!"

# Chamar função
nome = input("Informe o seu nome: ").strip().title()

print(mostrar_msg(nome))