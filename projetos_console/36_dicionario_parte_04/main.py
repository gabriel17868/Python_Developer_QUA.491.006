# dicionário
usuario = dict(nome="Gabriel Maraschin", idade=40, email="gabrielmaraschin123@gmail.com", profissão="programador")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

