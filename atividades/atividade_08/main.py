'''
# TODO - Atividade: Crie um programa que receba de um professor várias notas de um aluno de 0 a 10 (não importa quantas notas). Ao final do programa, a média das notas deverá ser calculada e informada, e em seguida, o programa irá informar se o aluno:
- Foi aprovado, caso média for maior ou igual a 7.
- Ficou de recuperação, caso média for entre 5 e 7.
- Foi reprovado, caso média for menor que 5.
'''
import os 

notas = []

while True:
    try:       
        print(f"{'-'*20} MENU {"-"*20}")
        print("1 - Informe uma nota do aluno de 0 a 10.")
        print("2 - Mostrar a média do aluno")
        print("3 - Mostrar as notas")
        opcao = input("Informe a opção desejada: ").strip()
        os.system("cls" if os.name =="nt" else "clear")

        match opcao:
            case "1":
                try:
                    nota_nova = float(input("Informe a nota do aluno: ").replace(",", "."))
                    if nota_nova >= 0 and nota_nova <= 10:
                        notas.append(nota_nova)
                        print("Nota cadastrada com suceso!")
                    else: 
                        print("Nota inválida.")
                except Exception as e:
                    print(f"Não foi possível Infomar a nota. {e}.")
                finally:
                    continue

            case "2":
                try:
                    media = sum(notas)/len(notas)
                    if media >= 7:
                        print(f"A média do aluno foi {media:.2f}, APROVADO!!!")
                    elif media >=5 and media <=7:
                        print(f"A média do aluno foi {media:.2f}, Recuperação :|")
                    else:
                        print(f"A média do aluno foi {media:.2f}, Reprovado :(")
                except Exception as e:
                    print(f"Não foi possível calcular a média. {e}.")
                finally:
                    break
            
            case "3":
                print(notas)
                continue
            
            case _:
                print("Opção inválida")
                
    except Exception as e:
        print(f"Não foi possível realizar requisição. {e}.")
    

