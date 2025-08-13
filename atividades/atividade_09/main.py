"""
# TODO - Atividade: Crie um programa que faça as seguintes funções:
- Cadastre um novo usuário
- Liste todos os usuários cadastrados
- Altere os dados de um usuário
- Fazer sorteio de usuário
- Exclua um usuário
- Saia do programa
# NOTE - Dados do Usuário:
- Nome Completo
- Data de Nascimento
- E-mail
- CPF
- Telefone
- Gênero
- Data do cadastro
- Hora do cadastro
"""
import os
import random
import datetime 
from datetime import date


usuarios = []

while True:
    try:       
        print(f"{'-'*20} MENU {"-"*20}")
        print("1 - Cadastrar novo usuário.")
        print("2 - Listar todos os usuários cadastrados")
        print("3 - Altere os dados de um usuário")
        print("4 - Sortear um usuário")
        print("5 - Excluir um usuário")
        print("6 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        os.system("cls" if os.name =="nt" else "clear")

        match opcao:
            case "1":
                try:

                    print("\n--- Cadastro de Novo Usuário ---")
                    nome = input("Nome completo: ").title().strip()
                    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
                    email = input("E-mail: ").strip()
                    cpf = input("CPF: ").strip()
                    telefone = input("Telefone: ").strip()
                    genero = input("Gênero: ").strip()
                    data = date.today().strftime("%d/%m/%Y")
                    hora = datetime.datetime.now().strftime("%H:%M:%S")

                    usuario = {
                        "nome": nome,
                        "nascimento": nascimento,
                        "email": email,
                        "cpf": cpf,
                        "telefone": telefone,
                        "genero": genero,
                        "data": data,
                        "hora": hora
                    }

                    usuarios.append(usuario)
                    print("Usuário cadastrado com sucesso!")

                except Exception as e:
                    print(f"Não foi possível cadastrar usuário. {e}.")
                finally:
                    continue

            case "2":
                try:
                    if not usuarios:
                        print("\nNenhum usuário cadastrado.")
                    else:
                        print("\n--- Lista de Usuários ---")
                        for i, usuario in enumerate(usuarios):
                            print(f"\nÍndice: {i}")
                            for chave, valor in usuario.items():
                                print(f"{chave.capitalize()}: {valor}")
                except Exception as e:
                    print(f"Não foi possível listar os usuários. {e}.")
                finally:
                    continue
            
            case "3":               
                if not usuarios:
                    print("\nNenhum usuário cadastrado para alterar.")
                else:
                    print("\n--- Lista de Usuários ---")
                    for i, usuario in enumerate(usuarios):
                        print(f"{i} - {usuario['nome']}")
                    try:
                        indice = int(input("Informe o indice do usuário que deseja alterar: "))
                        if  0 <= indice < len(usuarios):
                            continuar = "s"
                            while continuar == "s":
                                print("\nCampos disponíveis para alteração:")
                                for chave in usuarios[indice]:
                                    print(f"{chave.capitalize()}: {usuarios[indice][chave]}")

                                chave_escolhida = input("Informe a chave que deseja alterar: ").lower().strip()
                                if chave_escolhida in usuarios[indice]:
                                    novo_valor = input(f"Informe o novo valor de {chave_escolhida}: ").strip()
                                    usuarios[indice][chave_escolhida] = novo_valor
                                    print(f"Campo '{chave_escolhida}' alterado com sucesso!")                                    
                                else:
                                    print("Campo inválido.")
                                continuar = input("Deseja alterar outra chave: s/n ").lower().strip()      
                        else:       
                            print("Índice inválido.")    
                    except Exception as e:
                        print(f"Não foi possível listar os usuários. {e}.")
                    finally:
                        continue
            
            case "4":
                try:
                    if not usuarios:
                        print("\nNenhum usuário cadastrado para sortear.")
                    else:
                        i = random.randint(0, len(usuarios)-1)
                        print(f"Usuário sorteado: {i} - {usuarios[i]['nome']}")
                except Exception as e:
                    print(f"Não foi possível sortear os usuários. {e}.")
                finally:
                    continue
                
            case "5":
                try:
                    if not usuarios:
                        print("\nNenhum usuário cadastrado para alterar.")
                    else:
                        print("\n--- Lista de Usuários ---")
                        for i, usuario in enumerate(usuarios):
                            print(f"{i} - {usuario['nome']}")
                        indice = int(input("Informe o indice do usuário que deseja excluir: "))
                        if  0 <= indice < len(usuarios):
                            nome_excluido = usuarios[indice]['nome']
                            del(usuarios[indice])
                            print(f"Usuário {nome_excluido} excluído com sucesso!")
                        else:
                            print("Índice inválido.")
                except Exception as e:
                    print(f"Não foi possível excluir o usuário. {e}.")
                finally:
                    continue

            case "6":
                print("Programa encerrado")
                break

            case _:
                os.system("cls" if os.name =="nt" else "clear")
                print("Opção Inválida")
                continue  
                
    except Exception as e:
        print(f"Não foi possível realizar requisição. {e}.")

