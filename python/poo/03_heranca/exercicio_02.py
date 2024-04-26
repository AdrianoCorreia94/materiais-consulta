class Pessoa:
    def __init__(self, nome, peso, altura) -> None:
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {', '.join([f'{chave} : {valor}' for chave, valor in self.__dict__.items()])}"


class Fisica(Pessoa):
    def __init__(self, cpf, **kargs) -> None:
        super().__init__(**kargs)
        self.cpf = cpf


class Juridico(Pessoa):
    def __init__(self, cnpj, **kargs) -> None:
        super().__init__(**kargs)
        self.cnpj = cnpj


class Prestador(Juridico, Fisica):
    def __init__(self, codigo, **kargs) -> None:
        super().__init__(**kargs)
        self.codigo = codigo


pre = Prestador(codigo=1, nome='Marcia', peso=147, altura=1.78,
                cpf='123.456.789.00', cnpj='098.765.0001-11')

p1 = Pessoa('Fabio', 80, 1.32)

print(p1)

print(pre)