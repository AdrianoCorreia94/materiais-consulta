class Eletronico:
    def __init__(self, polegadas, marca, cor) -> None:
        self.polegadas = polegadas
        self.marca = marca
        self.cor = cor

    def __str__(self) -> str:
        return(f'{self.__class__.__name__} {",".join([f"{chave} : {valor}" for chave, valor in self.__dict__.items()])}')


class Notebook(Eletronico):
    def __init__(self, entradas_usb, **kargs) -> None:
        super().__init__(**kargs)
        self.entradas_usb = entradas_usb


class Smartphone(Eletronico):
    def __init__(self, camera_frontal, camera_traseira, **kargs) -> None:
        super().__init__(**kargs)
        self.camera_frontal = camera_frontal
        self.camera_traseira = camera_traseira


class Tablet(Smartphone, Eletronico):
    def __init__(self, **kargs) -> None:
        super().__init__(**kargs)


novo = Tablet(polegadas=10, marca='Apple', cor='Branco',
              camera_frontal='10px', camera_traseira='25px')
print(novo)
