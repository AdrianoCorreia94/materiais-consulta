from datetime import date, datetime

# data simples
d = date(2024, 4, 25)
print(d)  # exibir objeto d
print(d.day)  # exibir o dia
print(d.month)  # exibir o mes
print(d.year)  # exibir o ano


# AGORA
agora = datetime.now()
print(f'agora = {agora}')


# HOJE
hoje = datetime.today()
print(f'hoje = {hoje}')


