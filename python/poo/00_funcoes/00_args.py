def teste(**kargs): # parametros com chave valor
    print(kargs)


def cad(*args): # parametros como tupla
    return args


teste(nome='adriano', idade=30, status='casado') # passando argumentos chave = valor

c = cad('É', 'Nao é nao nao', 'nao faz assim rs', 43) # passando argumentos como tupla
print(c)
for x, y in enumerate(c):
    print(x, y)