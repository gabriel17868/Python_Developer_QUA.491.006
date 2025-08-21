from deep_translator import GoogleTranslator
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    tradutor = GoogleTranslator(source="auto", target="pt")


    try:
        with open(f"serial-murder-analysis.ipynb", "r", encoding="utf-8") as f:
            texto = f.read()

        texto_traduzido = tradutor.translate(texto)

        with open(f"serial-murder-analysis.ipynb", "w", encoding="utf-8") as f:
            f.write(texto_traduzido)

    except Exception as e:
        print(f"Não foi possível traduzir. {e}.")


if __name__ == "__main__":
    main()