# dicionário
usuario = {
    'nome': "Gabriel Maraschin",
    'idade': 27,
    'email': "gabrielmaraschin123@gmail.com",
}

# Exibe os valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# Adicionando nova chave
usuario['profissão'] = input("Informe a profissão: ").strip()

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
