"""
# TODO - Atividade: Crie um programa de aplicativo de banco, onde:
- O usuário cria uma conta no banco com os seguintes dados:
-- Titular da conta
-- CPF do titular
-- Agência
-- Número da conta
-- Saldo 
O usuário pode fazer no programa:
- Consultar dados
- Depositar valor
- Sacar valor
- Imprimir extrato (entende - se: gerar arquivo com os dados da conta)
- Sair do programa
# NOTE - O nome da classe é conta
"""
import funcao as fu
import classe as cl

if __name__ == "__main__":
    while True:
        try:

            print(f"{'-'*20} BANCO COBRA {"-"*20}")
            print("1 - Criar conta.")
            print("2 - Consultar dados.")
            print("3 - Depositar valor.")
            print("4 - Sacar valor.")
            print("5 - Imprimir extrato")
            print("6 - Sair do programa.")
            opcao = input("Informe a opção desejada: ").strip()

            fu.limpar_tela()

            match opcao:
                case "1":
                    titular = input("Informe o nome do titular: ").strip().title()
                    cpf = input("Informe o CPF: ").strip()
                    agencia = input("Informe a agência: ").strip()
                    conta = input("Informe o número da conta: ").strip()
                    saldo = float(input("Informe o saldo inicial: "))
                    conta = cl.Conta(titular, cpf, agencia, conta, saldo)
                    print("Conta criada com sucesso!")
                    input("\nPressione Enter para continuar...")

                case "2":
                    try:
                        if conta:
                            print("\nDados da conta: ")
                            print(conta.consultar())
                        else: 
                            print("Nenhuma conta criada.")
                        input("\nPressione Enter para continuar...")
                    except Exception as e:
                        print(f"Não foi possível consultar dados. {e}.")

                case "3":
                    try:
                        if conta:
                            valor = float(input("Informe o valor do depósito: ").replace(",","."))
                            if conta.depositar(valor):
                                print("Depósito realizado com sucesso!")
                            else:
                                print("Valor inválido.")
                        else:
                            print("Nenhuma conta cadastrada.")
                        input("\nPressione Enter para continuar...")
                    except Exception as e:
                        print(f"Não foi possível realizar depósito. {e}.")
                case "4":
                    try:
                        if conta:
                            valor = float(input("Informe o valor do saque: "))
                            if conta.sacar(valor):
                                print("Saque realizado com sucesso!")
                            else:
                                print("Saldo insuficiente ou valor inválido.")
                        else:
                            print("Nenhuma conta cadastrada.")
                        input("\nPressione Enter para continuar...")
                    except Exception as e:
                        print(f"Não foi possível realizar saque. {e}.")            
                case "5":
                    try:
                        if conta:
                            conta.salvar_extrato_em_json()
                            print(f"Extrato salvo como 'extrato_{conta.conta}.json'")
                        else:
                            print("Nenhuma conta cadastrada.")
                        input("\nPressione Enter para continuar...")
                    except Exception as e:
                        print(f"Não foi possível realizar saque. {e}.")
                case "6":
                    print("Programa encerrado")
                    break
                    
                case _:
                    print("Opção Inválida")
                    input("\nPressione Enter para continuar...")
                    continue  
        except Exception as e:
            print(f"Não foi possível realizar requisição. {e}.")
            input("\nPressione Enter para continuar...")