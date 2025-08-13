"""
# TODO - Atividade: crie um programa que calcule a área e a circunferência de um círculo.
# NOTE - Use lambda
"""
import os
import math

area = lambda r: math.pi * r**2

circunferencia = lambda r: 2 * math.pi * r

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    try:
        r = float(input("Informe o raio do círculo: ").replace(",","."))

        a = area(r)
        c = circunferencia(r)

        limpar()
        print(f"A circunferência do círculo é: {c:.2f} e a área é: {a:.2f}.")
    except Exception as e:
        print(f"Não foi possível calcular. {e}.")


