'''
# TODO - Atividade: Crie um programa wue faça as seguintes operações:
- Calcular área de um círculo
- Calcular tamanho de uma circunferência
- Sair do programa
# NOTE - Para cada loop, o programa deverá limpar o terminal
'''
import math as m
import os

while True:
    print(" ")
    print(f"{'-'*20} MENU{'-'*20}")
    print("1 - Calcular área de um círculo")
    print("2 - Calcular tamanho de uma circunferência")
    print("3 = Sair do programa")
    opcao = input("Informe a operação desejada: ").strip()
    os.system("cls" if os.name =="nt" else "clear")
    try:
        if opcao == "1" or opcao =="2":
            r = float(input("Imforme o valor do raio em cm: ").replace(",","."))
        else:
            pass
        os.system("cls" if os.name =="nt" else "clear")
        match opcao:
            case "1":
                area = m.pi * (r**2)
                print(" ")
                print(f"O valor da área do círculo com o raio informado de {r}cm, é de {area:.1f}cm")
                continue
            case "2":
                cir = (2*m.pi) * r
                print(" ")
                print(f"O valor da circunferência com o raio informado de {r}cm, é de {cir:.1f}cm")
                continue
            case "3":
                print("Você saiu do programa...")
                break
            case _:
                os.system("cls" if os.name =="nt" else "clear")
                print("Operador Inválido")
                continue
    except Exception as e:
            print(f"Não foi possível calcular. {e}.")
            continue
    



    '''while True:
            prosseguir = input("Deseja refazer? (s/n): ").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção inválida, por favor digite 's' para sim ou 'n' para não.")
            continue

            if prosseguir == "s":
                os.system("cls")
                continue
            elif prosseguir== "n":
                os.system("cls")
                break
            else:
                print("Opção inválida.")
                break


       match prosseguir:
            case "s":
                os.system("cls")
                continue
            case "n":
                os.system("cls")
                break
            case _:
                print("Opção inválida.")
                break '''