import json
import os

usuarios = []

while True:
    print("\nMenu:")
    print("1 - Cadastrar nova chave e novo dado.")
    print("2 - Cadastrar novo usuário.")
    print("3 - Salvar arquivo JSON.")
    print("4 - Fazer leitura do JSON.")
    print("5 - Sair do programa.")
    
    opcao = input("Informe a opção desejada: ")
    
    match opcao:
        case "1":
            if not usuarios:
                print("Nenhum usuário cadastrado ainda. Cadastre um usuário primeiro (opção 2).")
                continue

            print("\nUsuários disponíveis:")
            for idx, user in enumerate(usuarios):
                print(f"{idx + 1}: {user}")

            try:
                indice = int(input("Escolha o número do usuário para adicionar nova chave/dado: ")) - 1
                if 0 <= indice < len(usuarios):
                    chave = input("Digite a nova chave: ")
                    valor = input("Digite o valor: ")
                    usuarios[indice][chave] = valor
                    print("Chave e valor adicionados com sucesso.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

        case "2":
            nome = input("Digite o nome do novo usuário: ")
            email = input("Digite o e-mail do novo usuário: ")
            novo_usuario = {
                "nome": nome,
                "email": email
            }
            usuarios.append(novo_usuario)
            print("Usuário cadastrado com sucesso.")

        case "3":
            try:
                with open("usuarios.json", "w", encoding="utf-8") as f:
                    json.dump(usuarios, f, indent=4, ensure_ascii=False)
                print("Arquivo JSON salvo com sucesso.")
            except Exception as e:
                print(f"Não foi possível salvar o arquivo. {e}.")

        case "4":
            if os.path.exists("usuarios.json"):
                try:
                    with open("usuarios.json", "r", encoding="utf-8") as f:
                        usuarios = json.load(f)
                    print("Arquivo JSON lido com sucesso.")
                    for idx, user in enumerate(usuarios):
                        print(f"{idx + 1}: {user}")
                except Exception as e:
                    print(f"Erro ao ler o arquivo JSON. {e}.")
            else:
                print("Arquivo 'usuarios.json' não encontrado.")

        case "5":
            print("Programa encerrado!")
            break

        case _:
            print("Opção inválida. Tente novamente.")
