'''
# TODO - Atividade: Crie um programa que receba do usuário, o nome, o peso em Kg, e a altura em metros, e calcule o IMC (Índice de Massa Corporal) do usuário. O programa deve mostrar o valor do IMC arredondado para 2 casas decimais, e mostrar o diagnóstico do usuário com base nos seguintes valores:
# - Caso o IMC seja menor que 18.5 = Abaixo do peso.
# - Caso o IMC seja maior ou igual a 18.5 e menor que 25 = peso ideal.
# - Caso o IMC seja maior ou igual a 25'' e menor que 30 = acima do peso.
# - Caso o IMC seja maior ou igual a 30 e menor que 35 = obeso. 
# - Caso o IMC seja maior ou igual a 35 e menor que 40 = obesidade grau 2.
# - Caso o IMC seja maior ou igual a 40 = obesidade mórbidade.
# NOTE - O usuário deverá informar o encerramento do programa, ou seja, ele poderá repetir o cálculo quantas vezes quiser.'''

while True:
    try:
        nome = input("Informe o seu nome: ").title().strip()
        peso = float(input("Informe seu peso em Kg: ").replace(",","."))
        altura = float(input("Informe sua altura em metros: ").replace(",","."))
        imc = peso / (altura ** 2)
        if imc < 18.5:
            print(f"{nome}, seu IMC é {imc:.2f}. Diagnóstico: Abaixo do peso.")
        elif imc >= 18.5 and imc < 25:
            print(f"{nome}, seu IMC é {imc:.2f}. Diagnóstico: Peso ideal.")
        elif imc >= 25 and imc < 30:
            print(f"{nome}, seu IMC é {imc:.2f}. Diagnóstico: Acima do peso.")
        elif imc >= 30 and imc < 35:
            print(f"{nome}, seu IMC é {imc:.2f}. Diagnóstico: Obeso.")
        elif imc >= 35 and imc < 40:
            print(f"{nome}, seu IMC é {imc:.2f}. Diagnóstico: Obesidade grau 2.")
        else:
            print(f"{nome}, seu IMC é {imc:.2f}. Diagnóstico: Obesidade mórbida.")

        while True:
            prosseguir = input("Deseja refazer? (s/n): ").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção inválida, por favor digite 's' para sim ou 'n' para não.")
            continue
        match prosseguir:
            case "s":
                continue
            case "n":
                print("Programa encerrado")
                break
            case _:
                print("Opção inválida, encerrando o programa.")
                break
    except Exception as e:
        print(f"Não foi possível calcular o IMC. {e}.")
        continue