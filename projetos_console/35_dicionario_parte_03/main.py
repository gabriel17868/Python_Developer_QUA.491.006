# Dicionário
usuario = {
    'nome': "Gabriel Maraschin",
    'idade': 27,
    'email': "gabrielmaraschin123@gmail.com",
    'profissão': "programador"
}

# Exibe os valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

    