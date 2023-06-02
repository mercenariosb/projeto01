from datetime import datetime

datas= "2022-10-12"
datafmt = '%Y-%m-%d'

data = datetime(2022, 4, 20)

print(data)

data_2 = datetime.strptime(datas, datafmt) # você passa o str

print(data_2)