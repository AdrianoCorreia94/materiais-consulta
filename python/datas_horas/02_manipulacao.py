from datetime import date, datetime, timedelta


# adicionar uma semana a uma data
hoje = date.today()  # sem fuso horario
agora = datetime.now()  # data de agora com timezone (fuso horario), pode ser passado como arg

next_week = agora + timedelta(weeks=1)  # acrescentar uma semana
mid_week2 = agora + timedelta(weeks=.5)  # acrescentar meia semana
next_month = agora + timedelta(days=30)  # acrescentar 30 dias


# saidas
print(f'agora : {agora}\n')
# print(f'Proxima semana: {next_week}\n')
# print(f'Meia semana: {mid_week2}\n')
# print(f'1 MES: {next_month}\n')

# --------------------
