
class Animal:
    def __init__(self, tipo, raca, nro_patas):
        self.tipo = tipo
        self.raca = raca
        self.nro_patas = nro_patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {','.join([f'{chave}: {valor}'for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kargs):
        super().__init__(**kargs)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **kargs):
        super().__init__(**kargs)
        self.cor_bico = cor_bico


class Ornitorrinco(Mamifero, Ave):
    # def __init__(self, tipo, raca, nro_patas, cor_pelo):
    #    super().__init__(tipo, raca, nro_patas, cor_pelo)
    def __init__(self, **kargs):
        super().__init__(**kargs)


orn = Ornitorrinco(cor_pelo='preto', cor_bico='laranja',
                   tipo='orni', raca='ornito', nro_patas=2)

print(orn)
