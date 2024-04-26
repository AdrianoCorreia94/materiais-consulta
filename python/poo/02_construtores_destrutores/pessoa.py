class Pessoa:
    def __init__(self, nome, genero) -> None:
        self.nome = nome
        self.genero = genero

    # remove automaticamente logo apos realizar as funcoes da classe
    def __del__(self):
        print('removendo instancia')

a = Pessoa('adriano','Masculino')

