# Superclasse ou classe-pai

class Pessoa:
    # Construtor
    def __init__(self, telefone, endereco):
        self.telefone = telefone
        self.endereco = endereco

    # Método
    def exibir_dados(self):
        print(f"Telefone: {self.telefone}")
        print(f"Endereco: {self.endereco}")

# Subclasses ou classe-filha
class PessoaFisica(Pessoa):
    # Construtor
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(telefone, endereco)

    # Método
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        super().exibir_dados()

class PessoaJuridica(Pessoa):
    # Construtor
    def __init__(self, nome_fantasia, cnpj, telefone, endereco):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(telefone, endereco)

    # Método
    def exibir_dados(self):
        print(f"Nome da empresa: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()