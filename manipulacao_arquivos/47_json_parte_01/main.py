# Importações
import json

try:
    # Input
    arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()

    # Lê o json e desserializa em um dicionário
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Output
    print(f"{'-'*20} DADOS {'-'*20}\n")
    for dado in dados:
        for chave in dado:
            print(f"{chave.capitalize()}: {dado.get(chave)}")
        print(f"-"*40)
except Exception as e:
    print(f"Não foi possível ler arquivo JSON. {e}")