class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0


# metodo acessor

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor < 0:
            return 'Por favor, digite um valor positivo'
        self.__saldo += valor
        return 'Deposito realziado com sucesso'

    def sacar(self, valor):
        if valor < 0:
            return 'Por favor, digite um valor positivo'
        if valor > self.__saldo:
            return 'Saldo insuficiente'
        self.__saldo -= valor
        return 'Saque realziado com sucesso'


if __name__ == '__main__':
    cli_1 = Conta(1, 'Diego')
