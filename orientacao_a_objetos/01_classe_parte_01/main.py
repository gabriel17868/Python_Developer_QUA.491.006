# O py tá on
# Classe
class Pessoa:
    # Atributos
    nome = "Gabriel Maraschin"
    idade = 27
    telefone = "(61) 99999-9999"
    cpf = "123.456.789-12"
    email = "gabriel@gmail.com"

    # Métodos
    def apresentar(self):
        print(f"Olá, o meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu e-mail é {self.email}.")

# Programa principal
if __name__ == "__main__":
    # Instanciar classe
    usuario = Pessoa()

    # Objeto se apresenta
    usuario.apresentar()