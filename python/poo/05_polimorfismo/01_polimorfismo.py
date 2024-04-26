class Ave:
    def voar(self):
        print('Voando')


class Andorinha(Ave):
    def voar(self):
        super().voar()


class Pinguim(Ave):
    def voar(self):
        print('Pinguim nao voa')


def voa(obj):
    obj.voar()


voa(Andorinha())
voa(Pinguim())