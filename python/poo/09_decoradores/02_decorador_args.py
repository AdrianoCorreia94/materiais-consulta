def decorador(funcao):
    def envelope(*args):
        funcao(*args)
        return funcao(args)

    return envelope


@decorador
def funcao(lista_arg: list):
    for x in lista_arg:
        print(x)


lista = ['a', 'b', 'c']

funcao(lista)
