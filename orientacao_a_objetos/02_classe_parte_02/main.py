# classe
class Pessoa:
    # construtor
    def __init__(self, nome, idade, telefone, cpf, email):
        # atributos
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    # Método de ação
    def apresentar(self):
        return f"Olá, o meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu e-mail é {self.email}."
    
# algoritmo principal
if __name__ == "__main__":
    # instancia a classe
    usuario = Pessoa(
        nome="",
        idade=0,
        telefone="",
        cpf="",
        email=""
    )

    try: 
        # input
        usuario.nome = input("Informe seu nome: ").strip().title()
        usuario.idade = int(input("Informe sua idade: "))
        usuario.telefone = input("Informe seu telefone: ").strip()
        usuario.cpf = input("Informe seu cpf: ").strip()
        usuario.email = input("Informe seu email: ").strip().lower()    

        # chama o método
        print(usuario.apresentar())
        
    except Exception as e:
        print(f"Erro. {e}.")
