import math as m

# Exibe o número pi
print(f"Número do pi: {m.pi}.") 

# Raíz Quadrada
try:
    n = int(input("Informe um número inteiro: "))
    print(f"A raíz quadrada de {n} é {m.sqrt(n)}.")
except Exception as e:
    print(f"Não foi possível calcular a raíz quadrada. {e}.")
