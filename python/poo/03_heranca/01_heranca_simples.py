class Automovel:
    def __init__(self, cor, ano, nro_rodas):
        self.cor = cor
        self.ano = ano
        nro_rodas = nro_rodas

    def __str__(self):
        return f'{self.__class__.__name__} {", ".join([f"{chave}:{valor}" for chave, valor in self.__dict__.items()])} '

    def ligarMotor(self) -> str:
        print(f'ligando motor')


class Carro(Automovel):
    def __init__(self, cor, ano, nro_rodas, combustivel):
        super().__init__(cor, ano, nro_rodas)  # herdando atributos da classe pai
        self.combustivel = combustivel


class Moto(Automovel):
    def __init__(self, cor, ano, nro_rodas, cilindros):
        super().__init__(cor, ano, nro_rodas)  # herdando atributos da classe pai
        self.cilindros = cilindros


carro = Carro('Prata', 2020, 4, 'flex')
print(carro)
