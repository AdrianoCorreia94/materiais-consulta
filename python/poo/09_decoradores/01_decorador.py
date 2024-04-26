# 1 - decorador simples
# %%
def meu_decorador_1(funcao):
    def envelope():
        print('Antes de executar a funcao')
        funcao()
        print('Depois de executar a funcao')

    return envelope


def ola_mundo():
    print('ola mundo')


teste = meu_decorador_1(ola_mundo)
teste()

# ---------------------

# decorator clear code


def meu_decorador_2(funcao):
    def envelope():
        print('Antes de executar a funcao')
        funcao()
        print('Depois de executar a funcao')
    return envelope


@meu_decorador_2
def ola_mundo_2():
    print('ola mundo 2')


ola_mundo_2()
# ---------------------
