# implementando a classe date
# exemplo generico para entender funcionamento da classe date

class classe_Date():
    def __init__(self, ano: int, mes: int, dia: int):
        self.ano = ano
        self.mes = mes
        self.dia = dia

    def ano(self):
        return self.ano

    def mes(self):
        return self.mes

    def dia(self):
        return self.dia

    @property
    def date(self):
        return f'{self.ano}-{self.mes}-{self.dia}'


d = classe_Date(2024, 4, 25).date
print(d)