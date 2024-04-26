# importar functools
import functools


def decorador(funcao):
    @functools.wraps(funcao)  # usar o decorador do envelope
    def envelope(*args, **kargs):
        funcao(*args, **kargs)
        return funcao(args, kargs)

    return envelope


@decorador
def funcao(*args, **kargs):
    print(f'oi {args} {kargs}')


print(funcao.__name__)
