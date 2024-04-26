def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    operacao = (funcao(a, b))
    print(operacao)


exibir_resultado(321, 15, somar)
exibir_resultado(321, 15, subtrair)

soma = somar
print(soma(3, 1))
