import ContaCorrente as c

def main():
    # Instancia objeto da classe Conta
    cc = c.ContaCorrente(
        nome="Gabriel", 
        cpf="000.000.000-00", 
        email="gabriel@gmail.com", 
        profissao="Developer", 
        telefone="(61) 99999-9999",
        endereco="Brasília",
        salario=4500.0,
        agencia="001",
        numero="100.100-00",
        saldo=0.0
    )

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
                    cc.exibir_dados()
                case "2":
                    try:
                        if cc.numero:
                            valor = float(input("Informe o valor do depósito: ").replace(",","."))
                            if valor > 0:
                                cc.fazer_deposito(valor)
                                print("Depósito realizado com sucesso!")
                                cc.exibir_dados()  # Mostrar dados atualizados após saque
                            else:
                                print("Valor inválido.")
                            input("\nPressione Enter para continuar...")
                    except Exception as e:
                        print(f"Não foi possível realizar depósito. {e}.")
                case "3":
                    try:
                        if cc.numero:
                            valor = float(input("Informe o valor do saque: ").replace(",","."))
                            if valor > 0 and valor <= cc.saldo:
                                cc.fazer_saque(valor)
                                print("Saque realizado com sucesso!")
                                cc.exibir_dados()  # Mostrar dados atualizados após saque
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
