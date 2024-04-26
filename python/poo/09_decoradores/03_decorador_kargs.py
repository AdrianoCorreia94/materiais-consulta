
def decorador(funcao):
    def envelope(*args, **kargs):
        funcao(*args, **kargs)
        return funcao(args, kargs)

    return envelope


@decorador
def funcao(*args, **kargs):
    print(f'oi {args} {kargs}')


funcao(1, nome='adriano')
