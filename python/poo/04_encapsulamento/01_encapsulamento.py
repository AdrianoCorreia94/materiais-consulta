class Conta():
    def __init__(self, saldo, conta) -> None:
        # utiliza-se o _ para indicar atributo privado, ele so podera ser usado dentro da classe
        self._saldo = saldo
        self.conta = conta

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def consultar_saldo(self):
        print(f'{self.conta} saldo: {self._saldo}')


errado = Conta(200, 'conta_01') # nao posso utilizar fora da classe o atributo saldo
errado._saldo # nao posso utilizar fora da classe,pra ver saldo, devo utilizar o metodoo consultar saldo