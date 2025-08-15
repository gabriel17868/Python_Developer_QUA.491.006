from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str
    endereco: str

    @abstractmethod
    def __str__(self):
        pass