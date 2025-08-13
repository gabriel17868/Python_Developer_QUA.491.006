"""
# TODO - atividade: Faça um CRUD (Creat, Read, Update, Delete) em um JSON
Opções do menu:
- Criar novo arquivo JSON (usuário irá informar o diretório).
- Abrir arquivo JSON (usuário irá informar o diretório).
- Cadastrar novo usuário em um JSON.
- Listar todos os usuário de um arquivo JSON.
- Pesquisar usuário através do valor de uma chave em um arquivo JSON.
- Alterar dados de um usuário em um arquivo JSON.
- Deletar usuário de um arquivo JSON.
- Sair do programa
Dados do usuário>
- Nome
- Data de nascimento
- CPF
- E-mail
- Telefone
- Filme favorito do usuário
"""
import os
import json

usuarios = []
arquivo = ""
diretorio = ""

while True:
    try:
        os.system("cls" if os.name == "nt" else "clear")
        # Menu 
        if not arquivo:
            print("Nenhum arquivo aberto")
        else:
            print(f"O arquivo {arquivo} está aberto")
            
        print(f"{'-'*20} MENU {"-"*20}")
        print("1 - Criar novo arquivo JSON. ")
        print("2 - Abrir arquivo JSON.")
        print("3 - Cadastrar novo usuário em um JSON.")
        print("4 - Listar todos os usuário em um arquivo JSON.")
        print("5 - Pesquisar por um usuário em um arquivo JSON.")
        print("6 - Alterar dados de um usuário em um arquivo JSON.")
        print("7 - Deletar usuário de um arquivo JSON.")
        print("8 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()

        match opcao:
            case "1":
                arquivo = input("Informe o nome do arquivo: ")
                diretorio = input("Informe o diretório")

                with open(f"{diretorio}/{arquivo}.json", "w", encoding="utf-8") as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)
                os.system("cls" if os.name == "nt" else "clear")
                print("Arquivo criado com sucesso.")
                input("\nPressione Enter para continuar...")
            
            case "2":
                arquivo = input("Informe o nome do arquivo: ").strip().lower()
                diretorio = input("Informe o diretório: ").strip().lower()
                with open(f"{diretorio}/{arquivo}.json", "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    usuarios = dados
                os.system("cls" if os.name == "nt" else "clear")
                print("Arquivo aberto com sucesso")     
                input("\nPressione Enter para continuar...")

            case "3":
                try:
                    usuario = {}

                    usuario['nome'] = input("Informe o nome: ").strip().title()
                    usuario['data_nascimento'] = input("Informe a data de nascimento: ")
                    usuario['CPF'] = input("Informe o CPF: ")
                    usuario['email'] = input("Informe o email: ").strip().lower()
                    usuario['telefone'] = input("Informe o telefone: ").strip()
                    usuario['filme'] = input("Informe o filme favorito: ")

                    usuarios.append(usuario)
                           
                    with open(f"{diretorio}/{arquivo}.json", "w", encoding="utf-8") as f:
                        json.dump(usuarios, f, ensure_ascii=False, indent=4)
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Usuário cadastrado com sucesso.")            
                except Exception as e:
                    print(f"Não foi possível cadastrar usuário. {e}.")
                input("\nPressione Enter para continuar...")
            
            case "4":
                if not usuarios:
                    print("Nenhum usuário cadastrado.")
                else:
                    print(f"{'-'*20} USUÁRIOS {'-'*20}")
                    for i, usuario in enumerate(usuarios):
                        try:
                            print(f"\nÍndice: {i}")
                            for chave, valor in usuario.items():
                                print(f"    {chave.capitalize()}: {valor}")
                            print(f"{'-'*50}")
                        except Exception as e:
                            print(f"Erro ao exibir usuário no índice {i}: {e}")
                input("\nPressione Enter para continuar...")
            
            case "5":   
                os.system("cls" if os.name =="nt" else "clear")
                chave = input("Informe a chave para buscar (ex: nome, cpf, email): ").lower()
                valor = input("Informe o valor para buscar: ")

                encontrados = []

                for usuario in usuarios:
                    if usuario.get(chave, "").lower() == valor.lower():
                        encontrados.append(usuario)
                
                if encontrados:
                    for usuario in encontrados:
                        print("\n--- Usuário encontrado ---")
                        for chave, valor in usuario.items():
                            print(f"{chave.capitalize()}: {valor}")
                else:
                    print("Nenhum usuário encontrado com esse valor.")
                input("\nPressione Enter para continuar...")

            case "6":
                if not usuarios:
                    print("\nNenhum usuário cadastrado para alterar.")
                    input("\nPressione Enter para continuar...")
                    continue
                try:
                    indice = int(input("Informe o índice do usuário a ser alterado: "))
                    if 0 <= indice < len(usuarios):
                        usuario_alterado = usuarios[indice]
                        print("Usuário encontrado. Deixe em branco para manter o valor atual.")
                        usuario_alterado["nome"] = input(f"Nome ({usuario_alterado['nome']}): ") or usuario_alterado["nome"]
                        usuario_alterado["data_nascimento"] = input(f"Data de nascimento ({usuario_alterado['data_nascimento']}): ") or usuario_alterado["data_nascimento"]
                        usuario_alterado["CPF"] = input(f"CPF ({usuario_alterado['CPF']}): ") or usuario_alterado["CPF"]
                        usuario_alterado["email"] = input(f"E-mail ({usuario_alterado['email']}): ") or usuario_alterado["email"]
                        usuario_alterado["telefone"] = input(f"Telefone ({usuario_alterado['telefone']}): ") or usuario_alterado["telefone"]
                        usuario_alterado["filme"] = input(f"Filme favorito ({usuario_alterado['filme']}): ") or usuario_alterado["filme"]
                        with open(f"{diretorio}/{arquivo}.json", "w", encoding="utf-8") as f:
                            json.dump(usuarios, f, ensure_ascii=False, indent=4)
                        print("Usuário alterado com sucesso.")
                except Exception as e:
                    print(f"Não foi possível alterar os dados do usuário. {e}.")
                input("\nPressione Enter para continuar...")

            case "7":
                if not usuarios:
                    print("\nNenhum usuário cadastrado para excluir.")
                    continue
                try:
                    indice = int(input("Informe o índice do usuário a ser excluido: "))
                    if 0 <= indice < len(usuarios):
                        nome_excluido = usuarios[indice]["nome"]
                        del(usuarios[indice])
                        print(f"Usuário {nome_excluido} excluído com sucesso!")
                        with open(f"{diretorio}/{arquivo}.json", "w", encoding="utf-8") as f:
                            json.dump(usuarios, f, ensure_ascii=False, indent=4)
                        
                except Exception as e:
                    print(f"Não foi possível excluir o usuário. {e}.")
                input("\nPressione Enter para continuar...")
            
            case "8":
                print("Programa encerrado")
                break
            
            case _:
                print("Opção Inválida")
                input("\nPressione Enter para continuar...")
                continue  

    except Exception as e:
        print(f"Não foi possível realizar requisição. {e}.")
        input("\nPressione Enter para continuar...")


