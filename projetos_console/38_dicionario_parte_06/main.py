# dicionário
usuario = {
    'nome': "Gabriel Maraschin",
    'idade': 27,
    'email': "gabrielmaraschin123@gmail.com",
    'profissão': "programador"
}

# Exibe os valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-"*40)

# Usuário informa a chave que deseja alterar
chave = input("Informe a chave que deseja alterar: ").lower().strip()

# Usuário informa o valor da chave
if chave in usuario:
    usuario[chave] = input(f"Informe o novo valor de {chave}: ").strip()
else:
    print("Chave inexistente.")

# Exibe os valores novamente
print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
