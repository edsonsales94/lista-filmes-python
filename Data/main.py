from datetime import datetime, timedelta
from data_br import DatasBr

#cadastro = DatasBr()
#print(cadastro)

hoje = datetime.today()
amanha= datetime.today() + timedelta(days=1)

print(hoje - amanha)


'''hoje = DatasBr()
print(hoje.tempo_cadastro())'''

'''
hoje = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")

print(hoje)
print(hoje_formatada)
print(type(hoje_formatada))
'''


'''
data = datetime.now()
datahj = data.strftime('%d/%A/%Y %H:%M')
print(datahj)
'''