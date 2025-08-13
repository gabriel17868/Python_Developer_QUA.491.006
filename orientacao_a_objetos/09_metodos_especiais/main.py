import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="Gabriel Maraschin", idade=27)

    print(usuario)
    print(f"Idade: {len(usuario)}")

    # Destruição do objeto
    del(usuario)

    print(usuario)

if __name__ == "__main__":
    main()