class Bicicleta():
    def __init__(self, modelo: str, cor: str, valor: float, ano: int) -> None:
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.ano = ano

    def buzinar(self):
        print(f'{self.__str__()} está buzinando')

    def correr(self):
        print(f'{self.modelo} correndo')

    def parar(self):
        print(f'{self.modelo} parando')

    # tornar o retorno do objeto mais dinamico
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {','.join([f"{chave}, {valor}" for chave, valor in self.__dict__.items()])}'

#    def teste(self):
#        for chave, valor in self.__dict__.items():
#            print(chave, valor)


b1 = Bicicleta('SX', 'Azul', 299.99, 2010)
print(b1)
