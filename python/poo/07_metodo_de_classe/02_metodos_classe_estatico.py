# metodos de classe
'''
    está ligado a classe
    tem acesso a classe e nao ao objeto
    recebem parametro que apontam para a classe
    chamamos de cls ao inves de self
    usado para criar método de fabrica (retornam instancia da classe)
'''

# metodos estaticos
'''
    nao recebem primeiro argumento explicito
    nao é objeto da classe, nao podendo acessar ou modifica-la
    criar funcoes utilitárias (validacoes por exemplo)
'''


class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod  # indica que iremos usar metodo de classe
    def criar_com_idade(cls, ano_atual, ano_nascimento, nome):
        idade = ano_atual - ano_nascimento
        return cls(nome, idade)  # cria uma instancia da classe.

    @staticmethod  # criar metodo static
    def verificar_idade(idade):
        return 'Maior de idade' if idade > 17 else 'Menor de idade'

    def __str__(self) -> str:
        return f'{self.nome} esta com {self.idade} anos'


# criando instancia com metodo de classe
p1 = Pessoa.criar_com_idade(int(input('Ano atual:\n>')), int(input(
    'Ano Nascimento:\n>')), str(input("nome")))

# formas de chamar o metodo estatico
print(p1.verificar_idade(p1.idade))
print(Pessoa.verificar_idade(p1.idade))
