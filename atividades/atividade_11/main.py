"""
# TODO - Atividade: Crie um programa que receba do usuário um número inteiro e o programa calcula o valor da sequência de Fibonnaci para o número informado.
"""

import modulo as mo

if __name__ == "__main__":
    while True:
        try:
            print("1 - Calculare Fibonnaci")
            print("2 - Sair do programa")
            opcao = input("Escolha: ").strip()
            match opcao:
                case "1":
                    n = int(input("Informe um número para calcular Fibonnaci: "))
                    print(f"Fibonnaci({n}) = {mo.fibonacci(n)}")
                    continue
                case "2":
                    print("Programa encerrado.")
                    break
                case _:
                    print("Opção inválida.")
                    continue
        except Exception as e:
            print(f"Erro. {e}.")
            continue