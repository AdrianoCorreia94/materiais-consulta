# variaveis de classe e variaveis de instancia
class Aluno:
    escola = 'escola_A'  # variavel da classe

    def __init__(self, nome, matricula) -> None:
        self.nome = nome  # variavel de instancia
        self.matricula = matricula  # variavel de instancia

    def __str__(self) -> str:
        return f'{self.escola} \t{self.nome} \t{self.matricula}'


adriano = Aluno('adriano', 1234)
print(adriano)

gisa = Aluno('gislaine', 5678)
print(gisa)