from abc import ABC, abstractmethod


class Controle(ABC):
    # todos os metodos com essa assinatura sao obrigados a ser criado nas instancias
    @abstractmethod
    def ligar(self):
        print('Ligando')

    @abstractmethod
    def desligar(self):
        print(f'Desligando')

    def trocar_pilha(self):
        print(f'trocando pilha {self.__class__.__name__}')

    @property  # propriedade abstrata
    @abstractmethod
    def marca(self):
        pass


class ControleTv(Controle):
    pass

    def ligar(self):
        print('ligando')

    def desligar(self):
        print('Desligando')

    @property # instanciando a propriedade
    def marca(self) -> str:
        return 'LG'


tv = ControleTv()
tv.ligar()
tv.desligar()
tv.trocar_pilha()
print(tv.marca)
