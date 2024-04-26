from datetime import date, datetime

# strftime : transforma apresentacao da string
agora = datetime.now()

print(agora)

formatado = agora.strftime('%Y/%m/%d')  # formatando para somente data
print(formatado)  # apresentadando somente data

formatado_2 = agora.strftime('%h/%m')  # mes por extenso e numero do mes
print(formatado_2)

formatado_3 = agora.strftime('%H:%M')  # formatando hora e minuto
print(formatado_3)  # apresentando hora e minuto

formatado_4 = agora.strftime('%d/%m %H:%M')  # formatando dia/mes hora:minuto
print(formatado_4)
