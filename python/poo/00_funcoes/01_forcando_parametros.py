# forcando tipo de passagem de parametro

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    # a barra forca que o parametro passado antes dela seja do tipo posicional, ou seja
    # nao aceitara args do tipo chave valor
    print(modelo, ano, placa, marca, motor, combustivel)


teste_1 = criar_carro('Marea', 1979, 'abc-123', 'VW', 2.0, 'alcool')
# teste_1 = criar_carro(modelo='Marea', 1979, 'abc-123', 'VW', 2.0, 'alcool') # vai gerar erro, pois nao aceita chave valor como arg
teste_1 = criar_carro('Marea', 1979, 'abc-123', marca='VW',
                      motor=2.0, combustivel='alcool')


def criar_pessoa(*, nome, sobrenome, nacionalidade, naturalidade):
    # o asterisco indica que todos os args deve ser nomeados
    print(nome, sobrenome, nacionalidade, naturalidade)


# criar_pessoa('Dolores', 'Fuertes del Bariga', 'Brasil', 'Curitiba') # gera erro, pois os parametros nao estao nomeados
criar_pessoa(nome='Florisbela', sobrenome='Dolores',
             nacionalidade='Brazil', naturalidade='Joanopolis')


def pintar(cor, ponta, tom, /, *, tipo, formato):
    # formato misto, antes pode ser posicional, e depois somente nomeado
    print(cor, ponta, tom, tipo, formato)


pintar('Azul', .7, 'pastel', tipo='tinta', formato='manual')
