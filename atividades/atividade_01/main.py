'''
# TODO - atividade:
Crie um programa que receba do usuário o valor do etanol e da gasolina em reais, e informe para o usuário qual o melhor combustível para abastecer.
# NOTE - o usuário poderá informar várias vezes os valores, irá encerrar o programa quando desejar.
# NOTE - cálculo: compensa etanol caso ele tenha 70% do valor da gasolina.
# NOTE - DIVIRTAM-SE!!!
'''

while True:
    # Menu 
    print(f"{'-'*20} MENU {"-"*20}")
    print("1 - Calcular melhor combustível para abastecer ")
    print("2 - Encerrar o programa")

    operador = input("Informe a operação desejada: ").strip()

    match operador:
        case "1":
            try:
                # Entrada de dados
                gasolina = float(input("Informe o valor da gasolina: R$ ").replace(",","."))
                etanol = float(input("Informe o valor do etanol: R$ ").replace(",","."))
                vantagem = (etanol/gasolina)*100
                if vantagem < 70:
                     print(f"Valor do porcentual {vantagem:.2f}%, compensa a etanol")
                else:
                    print(f"Valor do porcentual {int(vantagem)}%, compensa o gasolina")
            except Exception as e:
                print(f"Não foi possível calcular. {e}.")
            finally:
                continue
        case "2":
            print("Programa encerrado")
            break

''' if etanol > gasolina*0.7:
         print(f"Valor do porcentual {vantagem}%, compensa a etanol")
    else:
        print(f"Valor do porcentual {vantagem}%, compensa o gasolina")
    except Exception as e:
        print(f"Não foi possível calcular. {e}.")
    finally:
        continue'''

'''
while True:
    gasolina = float(input("Informe o valor da gasolina: R$ ").replace(",","."))
    etanol = float(input("Informe o valor do etanol: R$ ").replace(",","."))
    result = "gasolina" if etanol > gasolina*0.7 else "etanol"
    print(f"Melhor combustível para abastecer: {result}")

    opcao = input("Deseja continuar? (s/n): ").strip().lower()
    match opcao:
        case "s":
            continue
        case "n":
            print("Programa encerrado")
            break
        case _:
            print("Opção inválida, encerrando o programa.")
            contienue
    except Exception as e:
            print(f"Não foi possível calcular. {e}.")
            continue
# Fim do código da atividade
'''