chaves = ("Nome", "Idade", "E-mail", "Telefone", "Profissão")
usuario = {
    chaves[0]: "Gabriel Maraschin",
    chaves[1]: 27,
    chaves[2]: "gabrielmaraschin123@gmail.com",
    chaves[3]: "(61) 98765-0000",
    chaves[4]: "programador"
}

for chave in chaves:
    print(f"{chave}: {usuario.get(chave)}")