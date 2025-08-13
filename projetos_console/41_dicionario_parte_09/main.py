usuarios = [
    {
        'nome': "Gabriel Maraschin",
        'idade': 27,
        'email': "gabrielmaraschin123@gmail.com"
    },
    {
        'nome': "Cicrano",
        'idade': 25,
        'email': "cigrano@gmail.com"
    },
    {
        'nome': "Beltrano",
        'idade': 30,
        'email': "beltrano@gmail.com"
    }
]

# Exibe os dados
for usuario in usuarios:
    print("-"*40)
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")