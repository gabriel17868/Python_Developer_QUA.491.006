# Superclasse
class Pessoa:
    def __init__(self, telefone, endereco):
        self.__telefone = telefone # private
        self.__endereco = endereco # private
    
    # métodos de acesso

    # método set telefone
    def telefone(self, telefone):
        self.__telefone = telefone