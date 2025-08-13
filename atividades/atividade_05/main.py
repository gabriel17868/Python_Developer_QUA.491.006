"""
# TODO - Atividade: Crie um programa que receba do usuário o nome e a idade, e em seguida, mostre um menu de filmes com suas respectivas classificações indicativas e salas de exibição. Exemplo:
- Sala 1: A Roda Quadrada - Livre
- Sala 2: A Volta dos Que Não Foram - 12 anos
- Sala 3: Poeira em Alto Mar - 14 anos
- Sala 4: As Tranças do Rei Careca - 16 anos
- Sala 5: A Vingança do Peixe Frito - 18 anos
O usuário deve Sala 5: A Vingança do Peixe Frito - 18 anos que está passando o filme que deseja assistir.
- Se o usuário tiver a idade mínima ou mais para ver o filme, o programa imprime o ingresso com o nome do usuário, a sala, o nome do filme, a data e a hora da compra do ingresso, e deseje bom filme, e em seguida, encerra o programa.
- Se o usuário não tiver a idade mínima para ver o filme, o programa bloqueia a sua entrada, e re-exibe o menu de filmes para que ele escolha outro filme.
"""
import os
import datetime 
from datetime import date


nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: "))
data = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")
os.system("cls" if os.name =="nt" else "clear")

while True:
    print(f"{'-'*20}FILMES{'-'*20}")
    print("Sala 1: A Roda Quadrada - Livre")
    print("Sala 2: A Volta dos Que Não Foram - 12 anos")
    print("Sala 3: Poeira em Alto Mar - 14 anos")
    print("Sala 4: As Tranças do Rei Careca - 16 anos")
    print("Sala 5: A Vingança do Peixe Frito - 18 anos")
    opcao = input("Informe o número da sala desejada: ").strip()
    os.system("cls" if os.name =="nt" else "clear")
    try:
        match opcao:
            case "1":
                print("Ingresso: ")
                print(f" Filme: A Roda Quadrada, cliente: {nome}. Data: {data}. Hora: {hora}")
                print("  Tenha um bom filme!!!")
                break
            case "2":
                if idade >= 12:
                    print("Ingresso: ")
                    print(f" Filme: A Volta dos Que Não Foram, cliente: {nome}. Data: {data}. Hora: {hora}")
                    print("  Tenha um bom filme!!!")
                    break
                else:
                    print("Cliente fora da classificação etária")
                    continue
            case "3":
                if idade >= 14:
                    print("Ingresso: ")
                    print(f" Filme: Poeira em Alto Mar, cliente: {nome}. Data: {data}. Hora: {hora}")
                    print("  Tenha um bom filme!!!")
                    break
                else:
                    print("Cliente fora da classificação etária ")
                    continue
            case "4":
                if idade >= 16:
                    print("Ingresso: ")
                    print(f" Filme: As Tranças do Rei Careca, cliente: {nome}. Data: {data}. Hora: {hora}")
                    print("  Tenha um bom filme!!!")
                    break
                else:
                    print("Cliente fora da classificação etária")
                    continue
            case "5":
                if idade >= 18:
                    print("Ingresso: ")
                    print(f" Filme: A Vingança do Peixe Frito, cliente: {nome}. Data: {data}. Hora: {hora}")
                    print("  Tenha um bom filme!!!")
                    break
                else:
                    print("Cliente fora da classificação etária")
                    continue
            case _:
                os.system("cls" if os.name =="nt" else "clear")
                print("Operador Inválido")
                continue        
    except Exception as e:
        print(f"Não foi possível realizar requisição. {e}.")
    

