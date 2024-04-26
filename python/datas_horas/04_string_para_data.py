# transformar string em data
import datetime

nascimento = '1994-01-15'
transformando_1 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d')  # transformar a string em datatime

transformando_2 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d').date()  # capturar data da string

transformando_3 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d').year  # capturar ano da string

transformando_4 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d').month  # capturar mes da string

transformando_5 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d').day  # capturar dia da string

transformando_6 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d').hour  # capturar hora da string

transformando_7 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d').minute  # capturar minutos da string

transformando_8 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d').second  # capturar segundos da string

transformando_9 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d').time()  # trasnformar da string em horas:min:seg

transformando_10 = datetime.datetime.strptime(
    nascimento, '%Y-%m-%d').ctime()  # data por extenso

print(transformando_1)
print(transformando_2)
print(transformando_3)
print(transformando_4)
print(transformando_5)
print(transformando_6)
print(transformando_7)
print(transformando_8)
print(transformando_9)
print(transformando_10)
