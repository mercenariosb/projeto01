from datetime import datetime
from pytz import timezone

datas= "2022-10-12"
datafmt = '%Y-%m-%d'

data = datetime(2022, 4, 20)

print(data)

data_2 = datetime.strptime(datas, datafmt) # você passa o str

print(data_2)

data3 = datetime.now(timezone('America/Sao_Paulo')) # data atual

print(data3)

#relative time delta bom ara pegar diferença de datas ja com 