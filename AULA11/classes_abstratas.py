from abc import ABC, abstractmethod


class funcionario(ABC):
    @abstractmethod
    def salario(self):
        pass


class vendedor(ABC):
    def salario(self):
        return 'cauculo 1'


class estagiario(ABC):
    def salario(self):
        return 'cauculo 2'
