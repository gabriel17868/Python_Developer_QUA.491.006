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

# Usuário informa chave que deseja excluir
chave = input("Informe a chave que deseja excluir: ").lower().strip()

# Verifica se a chave existe
if chave in usuario:
    # Exclui a chave
    del usuario[chave]
else:
    print("Chave inexistente")

# Exibe os valores novamente
print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")