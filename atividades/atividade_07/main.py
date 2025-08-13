"""
# TODO - Atividade: Crie um programa que faça as seguintes operações:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pesquise por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
- Sair do programa
# NOTE - a lista deve começar vazia. Exemplo: lista= []
"""
import os

nomes = []
while True:
    try:
        # Menu 
        print(f"{'-'*20} MENU {"-"*20}")
        print("1 - Cadastre novo nome")
        print("2 - Liste todos os nomes na lista")
        print("3 - Pesquise por um nome na lista")
        print("4 - Altere um nome na lista")
        print("5 - Exclua um nome na lista")
        print("6 - Sair do programa")
        # Informe a opção
        opcao = input("Informe a opção desejada: ").strip()
        os.system("cls" if os.name =="nt" else "clear")
        # lista
        match opcao:
            case "1":
                # Usuário informa nome a ser acrescentado na lista
                try:
                    novo_nome = input("Informe o novo nome: ").title().strip()
                    nomes.append(novo_nome)
                    print(f"{novo_nome} inserido com sucesso!")
                except Exception as e:
                    print(f"Não foi possível Infomar o nome. {e}.")
                finally:
                    continue

            case "2":
                # Exibe a lista
                try:
                    for i in range(len(nomes)):
                        print(f"{i}: {nomes[i]}.")
                    print(f"{'-'*46}")
                except Exception as e:
                    print(f"Não foi possível exibir a lista. {e}.")
                finally:
                    continue

            case "3":
                # Pesquise por um nome na lista
                try:
                    nome_pesquisada = input("Informe o nome a ser pesquisado: ").title().strip()
                    qtde = nomes.count(nome_pesquisada)
                    print(f"{nome_pesquisada} foi encontrado {qtde} vezes na lista.")
                except Exception as e:
                    print(f"Não foi possível pesquisar o nome. {e}.")
                finally:
                    continue

            case "4":
                # Altere um nome na lista
                try:
                    # Usuário informa a posição (índice)
                    i = int(input("Informe o índice a ser alterado: "))

                    if i >= 0 and i < len(nomes):
                        # Atualiza novo item na posição informada
                        nomes[i] = input("Informe o novo nome: ").title().strip()
                        os.system("cls" if os.name =="nt" else "clear")
                        print("Nome atualizado com sucesso!")
                    else:
                        print("Índice inválido")
                except Exception as e:
                    print(f"Não foi possível alterar. {e}.") 
                finally:
                    continue

            case "5":
                # Exclua um nome na lista
                try:
                    i = int(input("Informe a posição do nome na lista: "))
                    if i >= 0 and i < len(nomes):
                        # Exclui nome da lista
                        del(nomes[i])
                        os.system("cls" if os.name =="nt" else "clear")
                        print("Nome excluído com sucesso!")
                    else:
                        print("Índice inválido.")
                except Exception as e:
                    print(f"Não foi possível excluir o nome da lista {e}.")
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




