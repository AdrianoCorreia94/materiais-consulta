class Pessoa:
    def __init__(self, nome, ano_nascimento) -> None:
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property # torna a funcao um atributo
    def idade(self):
        return 2024 - self.ano_nascimento


p1 = Pessoa('Clodoaldo', 1994)
print(p1.idade) # posso chamar a funcao como um atributo
