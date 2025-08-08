import classes as c

def main():
    # Instancia objeto da classe Conta
    cc = c.ContaCorrente(
        titular="", 
        cpf="", 
        agencia="", 
        conta="", 
        saldo=0.0
    )


    
    cc.titular = input("Informe o nome: ").strip().title()
    cc.cpf = input("Informe o CPF: ").strip()
    cc.agencia = input("Informe a agencia: ")
    cc.conta = input("Informe a conta: ")
    cc.saldo = float(input("Informe o saldo: ").replace(",","."))

    while True:
        try:
            print(f"{'-'*20} BANCO COBRA {"-"*20}")
            print("1 - Consultar dados.")
            print("2 - Depositar valor.")
            print("3 - Sacar valor.")
            print("4 - Sair do programa.")
            opcao = input("Informe a opção desejada: ").strip()

            match opcao:
                case "1":
                    cc.consultar_dados()
                case "2":
                    try:
                        if cc.conta:
                            valor = float(input("Informe o valor do depósito: ").replace(",","."))
                            if valor > 0:
                                cc.depositar(valor)
                                print("Depósito realizado com sucesso!")
                                cc.consultar_dados()  # Mostrar dados atualizados após saque
                            else:
                                print("Valor inválido.")
                    except Exception as e:
                        print(f"Não foi possível realizar depósito. {e}.")
                case "3":
                    try:
                        if cc.conta:
                            valor = float(input("Informe o valor do saque: ").replace(",","."))
                            if valor > 0 and valor <= cc.saldo:
                                cc.sacar(valor)
                                print("Saque realizado com sucesso!")
                                cc.consultar_dados()  # Mostrar dados atualizados após saque
                            else:
                                print("Saldo insuficiente ou valor inválido.")
                        else:
                            print("Nenhuma conta cadastrada.")
                        input("\nPressione Enter para continuar...")
                    except Exception as e:
                        print(f"Não foi possível realizar depósito. {e}.")
                case "4":
                    print("Programa encerrado")
                    break
                case _:
                    print("Opção Inválida")
                    input("\nPressione Enter para continuar...")
                    continue  
        except Exception as e:
            print(f"Não foi possível realizar requisição. {e}.")
            input("\nPressione Enter para continuar...")
    

if __name__ == "__main__":
    main()