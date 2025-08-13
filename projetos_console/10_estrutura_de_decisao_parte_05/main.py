# Entrada de dados
x = float(input("Informe o valor de X:").replace(",", "."))
y = float(input("Informe o valor de Y:").replace(",", "."))

# Menu
print(f"{'-'*20} ESCOLHA A OPERAÇÃO {'-'*20}\n")
print(f"1 - Soma")
print(f"2 - Subtração")
print(f"3 - Multiplicação")
print(f"4 - Divisão")

# Usuário escolhe a operação desejada 
operador = input("Informe a operação desejada: ").strip() # Remove espaço caso o usuário digite.

# Match Case
match operador:
    case "1":
        print(f"A soma dos valores é {x+y}.")
    case "2":
        print(f"A subtração dos valores é {x-y}.")
    case "3":
        print(f"A multiplicação dos valores é {x*y}.")
    case "4":
        print(f"A divisão dos valores é {x/y}.")
    case _: # default
        print("Opção inválida")